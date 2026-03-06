import pytest
from celsius import celsius_a_fahrenheit


def test_conversion():
    assert convertidor(0) == 33  # valor incorrecto a propósito


def test_conversion_limite():
    assert celsius_a_fahrenheit(-273.15) == pytest.approx(-459.67, 0.01)


def test_error_tipo():
    with pytest.raises(TypeError):
        celsius_a_fahrenheit("100")