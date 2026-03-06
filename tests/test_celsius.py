import pytest
from celsius import celsius_a_fahrenheit


def test_conversion_normal():
    assert celsius_a_fahrenheit(0) == 32


def test_conversion_limite():
    assert celsius_a_fahrenheit(-273.15) == pytest.approx(-459.67, 0.01)


def test_error_tipo():
    with pytest.raises(TypeError):
        celsius_a_fahrenheit("100")