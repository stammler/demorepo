from typing import Type
from calculator import Calculator
import pytest


def test_addition_inputs():
    c = Calculator()
    with pytest.raises(TypeError):
        c.add("3", 2)
    with pytest.raises(TypeError):
        c.add("3", "2")
    with pytest.raises(TypeError):
        c.add(3, "2")


def test_subtraction_inputs():
    c = Calculator()
    with pytest.raises(TypeError):
        c.subtract("3", 2)


def test_division_inputs():
    c = Calculator()
    with pytest.raises(TypeError):
        c.divide("3", 2)


def test_multiplication_inputs():
    c = Calculator()
    with pytest.raises(TypeError):
        c.multiply("3", 2)


def test_zero_division_inputs():
    c = Calculator()
    with pytest.raises(ValueError):
        c.divide(3, 0)
