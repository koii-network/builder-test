import pytest
from src.arithmetic import add, subtract, multiply, divide

def test_add_positive_numbers():
    assert add(3, 5) == 8
    assert add(2.5, 3.7) == pytest.approx(6.2)

def test_add_negative_numbers():
    assert add(-3, -5) == -8
    assert add(-2.5, -3.7) == pytest.approx(-6.2)

def test_add_mixed_numbers():
    assert add(3, -5) == -2
    assert add(-2.5, 3.7) == pytest.approx(1.2)

def test_add_type_error():
    with pytest.raises(TypeError):
        add("3", 5)
    with pytest.raises(TypeError):
        add(3, "5")
    with pytest.raises(TypeError):
        add(None, 5)

def test_subtract_positive_numbers():
    assert subtract(10, 4) == 6
    assert subtract(10.5, 4.3) == pytest.approx(6.2)

def test_subtract_negative_numbers():
    assert subtract(-3, -5) == 2
    assert subtract(-2.5, -3.7) == pytest.approx(1.2)

def test_subtract_mixed_numbers():
    assert subtract(3, 5) == -2
    assert subtract(10.5, 4) == pytest.approx(6.5)

def test_subtract_type_error():
    with pytest.raises(TypeError):
        subtract("3", 5)
    with pytest.raises(TypeError):
        subtract(3, "5")
    with pytest.raises(TypeError):
        subtract(None, 5)

def test_multiply_positive_numbers():
    assert multiply(3, 5) == 15
    assert multiply(2.5, 4.0) == 10.0

def test_multiply_negative_numbers():
    assert multiply(-3, -5) == 15
    assert multiply(-2.5, -4.0) == 10.0

def test_multiply_mixed_numbers():
    assert multiply(3, -5) == -15
    assert multiply(-2.5, 4.0) == -10.0

def test_multiply_type_error():
    with pytest.raises(TypeError):
        multiply("3", 5)
    with pytest.raises(TypeError):
        multiply(3, "5")
    with pytest.raises(TypeError):
        multiply(None, 5)

def test_divide_positive_numbers():
    assert divide(10, 2) == 5.0
    assert divide(10.0, 4.0) == pytest.approx(2.5)

def test_divide_negative_numbers():
    assert divide(-10, -2) == 5.0
    assert divide(-10.0, -4.0) == pytest.approx(2.5)

def test_divide_mixed_numbers():
    assert divide(10, -2) == -5.0
    assert divide(-10.0, 4.0) == pytest.approx(-2.5)

def test_divide_type_error():
    with pytest.raises(TypeError):
        divide("3", 5)
    with pytest.raises(TypeError):
        divide(3, "5")
    with pytest.raises(TypeError):
        divide(None, 5)

def test_divide_zero_error():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
    with pytest.raises(ZeroDivisionError):
        divide(10.5, 0)