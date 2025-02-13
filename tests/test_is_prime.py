import pytest
from src.is_prime import is_prime

def test_prime_numbers():
    """Test known prime numbers."""
    prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for num in prime_nums:
        assert is_prime(num) == True, f"{num} should be prime"

def test_non_prime_numbers():
    """Test known non-prime numbers."""
    non_prime_nums = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15]
    for num in non_prime_nums:
        assert is_prime(num) == False, f"{num} should not be prime"

def test_large_prime():
    """Test a large prime number."""
    assert is_prime(104729) == True  # A large prime number

def test_large_non_prime():
    """Test a large non-prime number."""
    assert is_prime(104730) == False  # A large non-prime number

def test_negative_and_zero():
    """Test negative numbers and zero."""
    assert is_prime(-7) == False
    assert is_prime(0) == False
    assert is_prime(1) == False

def test_invalid_input():
    """Test invalid input types."""
    with pytest.raises(ValueError):
        is_prime(3.14)
    with pytest.raises(ValueError):
        is_prime("not a number")
    with pytest.raises(ValueError):
        is_prime(None)