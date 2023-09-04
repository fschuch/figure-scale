"""Test the unit conversion table."""
import pint
import pytest

from figure_scale.unit_conversion import (
    conversion_table,
    update_conversion_table,
)


@pytest.mark.parametrize("unit", conversion_table)
def test_convert_unit(unit):
    """Test that the conversion table is correct."""
    if unit == "pt":
        expected_value = 1.0 / 72.0
    else:
        ureg = pint.UnitRegistry()
        expected_value = ureg(unit).to("in").magnitude
    actual_value = 1.0 * conversion_table[unit]
    relative_error = abs(actual_value - expected_value) / expected_value
    assert relative_error < 1e-8


def test_update_conversion_table__success():
    """Test that the conversion table is correct."""
    assert "test" not in conversion_table
    try:
        update_conversion_table(test=1.0)
        assert conversion_table["test"] == 1.0
    finally:
        conversion_table.pop("test", None)


def test_update_conversion_table__negative_value():
    """Test that the conversion table is correct."""
    with pytest.raises(ValueError):
        update_conversion_table(test=-1.0)
    assert "test" not in conversion_table


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
