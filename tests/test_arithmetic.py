import pytest
from src.arithmetic import add, subtract, multiply, divide

def test_add_positive_numbers():
    assert add(3, 5) == 8
    assert add(0, 0) == 0
    assert add(-2, 2) == 0

def test_add_floating_point():
    assert add(3.5, 2.5) == 6.0
    assert add(-1.5, 1.5) == 0

def test_add_invalid_input():
    with pytest.raises(TypeError):
        add("3", 5)
    with pytest.raises(TypeError):
        add(3, "5")
    with pytest.raises(TypeError):
        add(None, 5)

def test_subtract_positive_numbers():
    assert subtract(10, 5) == 5
    assert subtract(0, 0) == 0
    assert subtract(5, 10) == -5

def test_subtract_floating_point():
    assert subtract(5.5, 2.5) == 3.0
    assert subtract(-1.5, 1.5) == -3.0

def test_subtract_invalid_input():
    with pytest.raises(TypeError):
        subtract("10", 5)
    with pytest.raises(TypeError):
        subtract(10, "5")
    with pytest.raises(TypeError):
        subtract(None, 5)

def test_multiply_positive_numbers():
    assert multiply(3, 5) == 15
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6

def test_multiply_floating_point():
    assert multiply(2.5, 2) == 5.0
    assert multiply(-1.5, 2) == -3.0

def test_multiply_invalid_input():
    with pytest.raises(TypeError):
        multiply("3", 5)
    with pytest.raises(TypeError):
        multiply(3, "5")
    with pytest.raises(TypeError):
        multiply(None, 5)

def test_divide_positive_numbers():
    assert divide(10, 5) == 2
    assert divide(0, 5) == 0
    assert divide(-10, 5) == -2

def test_divide_floating_point():
    assert divide(5.0, 2) == 2.5
    assert divide(-7.5, 2.5) == -3.0

def test_divide_invalid_input():
    with pytest.raises(TypeError):
        divide("10", 5)
    with pytest.raises(TypeError):
        divide(10, "5")
    with pytest.raises(TypeError):
        divide(None, 5)

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)