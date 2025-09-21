import math
import pytest
from calc.calculator import (
    add, subtract, multiply, divide,
    power, modulo, floor_divide, absolute, sqrt
)

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5
    assert math.isclose(divide(7, 2), 3.5)

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(9, 0.5) == 3

def test_modulo():
    assert modulo(10, 3) == 1
    with pytest.raises(ZeroDivisionError):
        modulo(1, 0)

def test_floor_divide():
    assert floor_divide(7, 2) == 3
    assert floor_divide(-7, 2) == -4
    with pytest.raises(ZeroDivisionError):
        floor_divide(1, 0)

def test_absolute():
    assert absolute(-5) == 5
    assert absolute(3) == 3

def test_sqrt():
    assert sqrt(9) == 3
    assert math.isclose(sqrt(2), math.sqrt(2))
    with pytest.raises(ValueError):
        sqrt(-1)
