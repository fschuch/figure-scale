"""Test the core module."""
import matplotlib.pyplot as plt
import pytest

from figure_scale.core import GOLDEN_RATIO, FigSize, FigureScale


def test_fig_size_on_figure():
    """Test that the figure scale works on a figure."""
    figsize = FigSize(1.0, 1.0)
    fig, _ = plt.subplots(figsize=figsize)
    expected_size = (1.0, 1.0)
    actual_size = tuple(fig.get_size_inches())
    assert actual_size == expected_size


def test_fig_size_on_config():
    """Test that the figure scale works on config context."""
    figsize = FigSize(1.0, 1.0)
    with plt.rc_context({"figure.figsize": figsize}):
        fig, _ = plt.subplots()
        expected_size = (1.0, 1.0)
        actual_size = tuple(fig.get_size_inches())
        assert actual_size == expected_size


def test_golden_ration():
    """Test that the golden ratio is correct."""
    expected_ratio = 0.618
    actual_ratio = round(GOLDEN_RATIO, 3)
    assert actual_ratio == expected_ratio


class TestFigureScale:
    """Test the FigureScale class."""

    @pytest.fixture()
    def fig_scale(self):
        """Return a figure scale instance."""
        return FigureScale(1.0, 1.0)

    def test_fig_size_iter(self, fig_scale):
        """Test that the figure size is iterable."""
        expected_size = (1.0, 1.0)
        actual_size = tuple(fig_scale)
        assert actual_size == expected_size

    def test_fig_size_relative_height(self):
        """Test that the figure size is iterable."""
        fig_scale = FigureScale(width=2.0, aspect=0.5)
        expected_size = (2.0, 1.0)
        actual_size = tuple(fig_scale)
        assert actual_size == expected_size

    def test_fig_size_relative_width(self):
        """Test that the figure size is iterable."""
        fig_scale = FigureScale(height=1.0, aspect=0.5)
        expected_size = (2.0, 1.0)
        actual_size = tuple(fig_scale)
        assert actual_size == expected_size

    def test_fig_size_getitem(self, fig_scale):
        """Test that the figure size is iterable."""
        expected_size = (1.0, 1.0)
        actual_size = fig_scale[:]
        assert actual_size == expected_size

    def test_fig_size_replace(self, fig_scale):
        """Test that the figure size is iterable."""
        expected_size = (2.0, 1.0)
        actual_size = tuple(fig_scale.replace(width=2.0))
        assert actual_size == expected_size

    def test_fig_size_len(self, fig_scale):
        """Test that the figure size has a length."""
        assert len(fig_scale) == 2

    def test_fig_size__invalid_units(self):
        """Test value error is raised for an unknown unit."""
        with pytest.raises(ValueError):
            FigureScale(1.0, 1.0, unit="invalid")

    def test_fig_size__units_conversion(self):
        """Test that the figure size is iterable."""
        fig_scale = FigureScale(1.0, 1.0, unit="ft")
        expected_size = (12, 12)
        actual_size = tuple(fig_scale)
        assert actual_size == expected_size

    def test_fig_size__on_figure(self):
        """Test that the figure size is iterable."""
        fig_scale = FigureScale(1.0, 1.0)
        fig, _ = plt.subplots(figsize=fig_scale)
        expected_size = (1.0, 1.0)
        actual_size = tuple(fig.get_size_inches())
        assert actual_size == expected_size

    def test_fig_size__on_config(self):
        """Test that the figure size is iterable."""
        fig_scale = FigureScale(1.0, 1.0)
        with plt.rc_context({"figure.figsize": fig_scale}):
            fig, _ = plt.subplots()
            expected_size = (1.0, 1.0)
            actual_size = tuple(fig.get_size_inches())
            assert actual_size == expected_size

    def test_fig_size__on_context(self, fig_scale):
        """Test that the figure size is iterable."""
        with fig_scale():
            fig, _ = plt.subplots()
            expected_size = (1.0, 1.0)
            actual_size = tuple(fig.get_size_inches())
            assert actual_size == expected_size

    def test_fig_size__on_decorator(self, fig_scale):
        """Test that the figure size is iterable."""

        @fig_scale()
        def my_fig():
            fig, _ = plt.subplots()
            return fig

        fig = my_fig()
        expected_size = (1.0, 1.0)
        actual_size = tuple(fig.get_size_inches())
        assert actual_size == expected_size
