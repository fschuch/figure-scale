"""Test the unit conversion table."""
from unittest import mock

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


@pytest.fixture()
def mocked_conversion_table():
    """Mock the conversion table."""
    with mock.patch.dict(
        "figure_scale.unit_conversion.conversion_table", {}
    ) as mocked:
        yield mocked


def test_update_conversion_table__success(mocked_conversion_table):
    """Test that the conversion table is correct."""
    assert "test" not in mocked_conversion_table

    update_conversion_table(test=1.0)
    assert mocked_conversion_table["test"] == 1.0


def test_update_conversion_table__negative_value(mocked_conversion_table):
    """Test that the conversion table is correct."""
    with pytest.raises(ValueError):
        update_conversion_table(test=-1.0)
    assert "test" not in mocked_conversion_table


def test_update_conversion_table__key_not_string(mocked_conversion_table):
    """Test that the conversion table is correct."""
    with pytest.raises(TypeError):
        update_conversion_table(**{10: 20})
    assert 10 not in mocked_conversion_table


def test_update_conversion_table__value_not_float(mocked_conversion_table):
    """Test that the conversion table is correct."""
    with pytest.raises(TypeError):
        update_conversion_table(test="1.0")
    assert "test" not in mocked_conversion_table


def test_update_conversion_table__overwrite(mocked_conversion_table):
    """Test that the conversion table is correct."""
    mocked_conversion_table["test"] = 1.0
    with pytest.raises(ValueError):
        update_conversion_table(test=2.0)
    assert mocked_conversion_table["test"] == 1.0
