import pytest
from src.factorial import calculate_factorial

def test_factorial_zero():
    assert calculate_factorial(0) == 1

def test_factorial_one():
    assert calculate_factorial(1) == 1

def test_factorial_positive():
    assert calculate_factorial(5) == 120
    assert calculate_factorial(3) == 6

def test_factorial_large_number():
    assert calculate_factorial(10) == 3628800

def test_factorial_negative_input():
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
        calculate_factorial(-1)

def test_factorial_non_integer_input():
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_factorial(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_factorial("5")