from calculator import Calculator


def test_addition():
    c = Calculator()
    assert 5 == c.add(3, 2)


def test_subtraction():
    c = Calculator()
    assert 1 == c.subtract(3, 2)


def test_multiplication():
    c = Calculator()
    assert 6 == c.multiply(3, 2)


def test_division():
    c = Calculator()
    assert 1.5 == c.divide(3, 2)
