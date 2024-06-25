"""Module containing the core functionality of the project."""

from __future__ import annotations

from collections.abc import Sequence
from contextlib import contextmanager
from dataclasses import dataclass, field, fields, replace
from operator import attrgetter
from typing import NamedTuple

from matplotlib.pyplot import rc_context

from figure_scale.unit_conversion import conversion_table


class FigSize(NamedTuple):
    """A named tuple to hold figure size information."""

    width: float
    height: float

    @classmethod
    def from_aspect(
        cls,
        width: float | None = None,
        height: float | None = None,
        aspect: float | None = None,
    ) -> FigSize:
        """Create a figure size from an aspect ratio, width, or height."""
        if sum(1 for v in (aspect, width, height) if v is not None) != 2:
            raise ValueError(
                "Exactly two out of width, height and aspect must be provided."
            )

        return cls(width or height / aspect, height or width * aspect)

    def rescale(self, factor: float) -> FigSize:
        """Rescale the figure size by a factor."""
        return self.__class__(*(i * factor for i in self))


GOLDEN_RATIO = (5.0**0.5 - 1.0) / 2.0
"""The golden ratio."""


@dataclass(frozen=True, repr=False, eq=False)
class FigureScale(Sequence):
    """Class to hold figure scale information."""

    width: float | None = None
    height: float | None = None
    aspect: float | None = None
    unit: str = "in"

    figsize: FigSize = field(init=False, repr=False)

    def __post_init__(self):
        """Validate the values."""
        try:
            factor = conversion_table[self.unit]
        except KeyError as err:
            raise ValueError(
                "Unknown unit: {}. The available options are: {}".format(
                    self.unit, ", ".join(conversion_table.keys())
                )
            ) from err

        try:
            width_abs = self.width or self.height / self.aspect
            height_abs = self.height or self.width * self.aspect
        except TypeError as err:
            raise ValueError(
                "Either width or height must be provided."
            ) from err

        figsize = FigSize(width_abs * factor, height_abs * factor)

        if any(value <= 0.0 for value in figsize):
            raise ValueError(
                "The figure size must be positive, please check your inputs."
            )

        object.__setattr__(self, "figsize", figsize)

    @contextmanager
    def __call__(self, **kwargs):
        """Replace the attributes of the figure scale."""
        with rc_context({**kwargs, "figure.figsize": self}):
            yield

    def __getitem__(self, index: slice | int):
        """Get the figure size."""
        return self.figsize[index]

    def __len__(self) -> int:
        """Return the length of the figure size."""
        return len(self.figsize)

    def __repr__(self):
        """Return a string representation of the figure scale."""
        nodef_f_vals = (
            (f.name, attrgetter(f.name)(self))
            for f in fields(self)
            if attrgetter(f.name)(self) != f.default and f.repr is True
        )

        nodef_f_repr = ", ".join(
            f"{name}={value}" for name, value in nodef_f_vals
        )
        return f"{self.__class__.__name__}({nodef_f_repr})"

    def replace(self, **kwargs) -> FigureScale:
        """Replace the attributes of the figure scale."""
        # TODO: rescale width and height if the unit is changed
        # so that the absolute size is the same
        return replace(self, **kwargs)
