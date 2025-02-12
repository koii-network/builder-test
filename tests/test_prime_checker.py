import sys
import os
import pytest

# Add the src directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from prime_checker import is_prime

def test_prime_numbers():
    # Test known prime numbers
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for num in prime_numbers:
        assert is_prime(num) == True, f"{num} should be prime"

def test_non_prime_numbers():
    # Test known non-prime numbers
    non_prime_numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
    for num in non_prime_numbers:
        assert is_prime(num) == False, f"{num} should not be prime"

def test_large_prime():
    # Test a large prime number
    assert is_prime(104729) == True, "104729 should be prime"

def test_invalid_input_type():
    # Test invalid input types
    with pytest.raises(TypeError):
        is_prime("not a number")
    with pytest.raises(TypeError):
        is_prime(3.14)
    with pytest.raises(TypeError):
        is_prime(None)

def test_invalid_input_range():
    # Test invalid input ranges
    with pytest.raises(ValueError):
        is_prime(1)
    with pytest.raises(ValueError):
        is_prime(0)
    with pytest.raises(ValueError):
        is_prime(-5)