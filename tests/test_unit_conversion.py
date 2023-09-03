"""Test the unit conversion table."""
import pint
import pytest

from figure_scale.unit_conversion import (
    CONVERSION_TABLE,
    update_conversion_table,
)


@pytest.mark.parametrize("unit", CONVERSION_TABLE)
def test_convert_unit(unit):
    """Test that the conversion table is correct."""
    if unit == "pt":
        return
    ureg = pint.UnitRegistry()
    actual_value = 1.0 * CONVERSION_TABLE[unit]
    expected_value = ureg(unit).to("in").magnitude
    relative_error = abs(actual_value - expected_value) / expected_value
    assert relative_error < 1e-8


def test_convert_unit__point_typography():
    """Test that the conversion table is correct."""
    actual_value = 72.0 * CONVERSION_TABLE["pt"]
    expected_value = 1.0
    relative_error = abs(actual_value - expected_value) / expected_value
    assert relative_error < 1e-8


def test_update_conversion_table__success():
    """Test that the conversion table is correct."""
    assert "test" not in CONVERSION_TABLE
    update_conversion_table(test=1.0)
    assert CONVERSION_TABLE["test"] == 1.0


def test_update_conversion_table__negative_value():
    """Test that the conversion table is correct."""
    with pytest.raises(TypeError):
        update_conversion_table(test=-1.0)
    assert "test" not in CONVERSION_TABLE


def test_update_conversion_table__key_not_string():
    """Test that the conversion table is correct."""
    with pytest.raises(TypeError):
        update_conversion_table(**{10: 20})


def test_update_conversion_table__value_not_float():
    """Test that the conversion table is correct."""
    with pytest.raises(TypeError):
        update_conversion_table(test="1.0")


def test_update_conversion_table__overwrite():
    """Test that the conversion table is correct."""
    with pytest.raises(ValueError):
        update_conversion_table(ft=1.0)
