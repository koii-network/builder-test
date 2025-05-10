import pytest
from src.arithmetic import add, subtract, multiply, divide

def test_add_positive_numbers():
    assert add(3, 5) == 8
    assert add(2.5, 3.5) == 6.0

def test_add_negative_numbers():
    assert add(-3, -5) == -8
    assert add(-2.5, -3.5) == -6.0

def test_add_mixed_numbers():
    assert add(-3, 5) == 2
    assert add(2.5, -3.5) == -1.0

def test_add_invalid_inputs():
    with pytest.raises(TypeError):
        add("3", 5)
    with pytest.raises(TypeError):
        add(3, "5")
    with pytest.raises(TypeError):
        add(None, 5)

def test_subtract_positive_numbers():
    assert subtract(8, 3) == 5
    assert subtract(8.5, 3.5) == 5.0

def test_subtract_negative_numbers():
    assert subtract(-8, -3) == -5
    assert subtract(-8.5, -3.5) == -5.0

def test_subtract_mixed_numbers():
    assert subtract(3, 8) == -5
    assert subtract(2.5, 3.5) == -1.0

def test_subtract_invalid_inputs():
    with pytest.raises(TypeError):
        subtract("8", 3)
    with pytest.raises(TypeError):
        subtract(8, "3")
    with pytest.raises(TypeError):
        subtract(None, 3)

def test_multiply_positive_numbers():
    assert multiply(3, 5) == 15
    assert multiply(2.5, 4.0) == 10.0

def test_multiply_negative_numbers():
    assert multiply(-3, -5) == 15
    assert multiply(-2.5, -4.0) == 10.0

def test_multiply_mixed_numbers():
    assert multiply(-3, 5) == -15
    assert multiply(2.5, -4.0) == -10.0

def test_multiply_invalid_inputs():
    with pytest.raises(TypeError):
        multiply("3", 5)
    with pytest.raises(TypeError):
        multiply(3, "5")
    with pytest.raises(TypeError):
        multiply(None, 5)

def test_divide_positive_numbers():
    assert divide(15, 3) == 5.0
    assert divide(10.0, 2.5) == 4.0

def test_divide_negative_numbers():
    assert divide(-15, -3) == 5.0
    assert divide(-10.0, -2.5) == 4.0

def test_divide_mixed_numbers():
    assert divide(15, -3) == -5.0
    assert divide(-10.0, 2.5) == -4.0

def test_divide_invalid_inputs():
    with pytest.raises(TypeError):
        divide("15", 3)
    with pytest.raises(TypeError):
        divide(15, "3")
    with pytest.raises(TypeError):
        divide(None, 3)

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
    with pytest.raises(ZeroDivisionError):
        divide(0, 0)