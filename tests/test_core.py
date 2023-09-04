"""Test the core module."""
import matplotlib.pyplot as plt
import pytest

from figure_scale.core import FigSize, FigureScale


def test_fig_size_on_figure():
    """Test that the figure scale works on a figure."""
    figsize = FigSize(1.0, 1.0)
    fig, _ = plt.subplots(figsize=figsize)
    expected_size = (1.0, 1.0)
    actual_size = tuple(fig.get_size_inches())
    assert actual_size == expected_size


def test_fig_size_on_config():
    """Test that the figure scale works on a figure."""
    figsize = FigSize(1.0, 1.0)
    with plt.rc_context({"figure.figsize": figsize}):
        fig, _ = plt.subplots()
        expected_size = (1.0, 1.0)
        actual_size = tuple(fig.get_size_inches())
        assert actual_size == expected_size


class TestFigureScale:
    """Test the FigureScale class."""

    fig_scale = FigureScale(1.0, 1.0)

    def test_fig_size_iter(self):
        """Test that the figure size is iterable."""
        expected_size = (1.0, 1.0)
        actual_size = tuple(self.fig_scale)
        assert actual_size == expected_size

    def test_fig_size_relative_hight(self):
        """Test that the figure size is iterable."""
        fig_scale = FigureScale(2.0, height_rel=0.5)
        expected_size = (2.0, 1.0)
        actual_size = tuple(fig_scale)
        assert actual_size == expected_size

    def test_fig_size_getitem(self):
        """Test that the figure size is iterable."""
        expected_size = (1.0, 1.0)
        actual_size = self.fig_scale[:]
        assert actual_size == expected_size

    def test_fig_size_replace(self):
        """Test that the figure size is iterable."""
        expected_size = (2.0, 1.0)
        actual_size = tuple(self.fig_scale.replace(width=2.0))
        assert actual_size == expected_size

    def test_fig_size_len(self):
        """Test that the figure size has a length."""
        assert len(self.fig_scale) == 2

    def test_fig_size__invalid_units(self):
        """Test value error is raised for an unknown unit."""
        with pytest.raises(ValueError):
            FigureScale(1.0, 1.0, units="invalid")

    def test_fig_size__units_conversion(self):
        """Test that the figure size is iterable."""
        fig_scale = FigureScale(1.0, 1.0, units="ft")
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

    def test_fig_size__on_context(self):
        """Test that the figure size is iterable."""
        with self.fig_scale():
            fig, _ = plt.subplots()
            expected_size = (1.0, 1.0)
            actual_size = tuple(fig.get_size_inches())
            assert actual_size == expected_size

    def test_fig_size__on_decorator(self):
        """Test that the figure size is iterable."""

        @self.fig_scale()
        def my_fig():
            fig, _ = plt.subplots()
            return fig

        fig = my_fig()
        expected_size = (1.0, 1.0)
        actual_size = tuple(fig.get_size_inches())
        assert actual_size == expected_size
