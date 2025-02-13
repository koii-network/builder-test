import pytest
from src.prime_checker import is_prime

def test_prime_numbers():
    # Test known prime numbers
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for num in prime_numbers:
        assert is_prime(num) == True, f"{num} should be prime"

def test_non_prime_numbers():
    # Test known non-prime numbers
    non_prime_numbers = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15]
    for num in non_prime_numbers:
        assert is_prime(num) == False, f"{num} should not be prime"

def test_large_prime():
    # Test a large prime number
    assert is_prime(97) == True
    assert is_prime(541) == True

def test_large_non_prime():
    # Test a large non-prime number
    assert is_prime(100) == False
    assert is_prime(999) == False

def test_invalid_input():
    # Test invalid input types
    with pytest.raises(ValueError):
        is_prime(3.14)
    with pytest.raises(ValueError):
        is_prime("not a number")
    with pytest.raises(ValueError):
        is_prime([])