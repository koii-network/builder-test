import pytest
from src.factorial import calculate_factorial

def test_factorial_zero():
    """Test factorial of 0 returns 1"""
    assert calculate_factorial(0) == 1

def test_factorial_one():
    """Test factorial of 1 returns 1"""
    assert calculate_factorial(1) == 1

def test_factorial_positive_numbers():
    """Test factorial for several positive numbers"""
    test_cases = [
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720)
    ]
    for num, expected in test_cases:
        assert calculate_factorial(num) == expected

def test_factorial_negative_number():
    """Test that a negative number raises a ValueError"""
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
        calculate_factorial(-1)

def test_factorial_non_integer():
    """Test that non-integer inputs raise a TypeError"""
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_factorial(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_factorial("5")
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_factorial(None)