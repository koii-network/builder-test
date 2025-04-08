import pytest
from src.prime_checker import is_prime

def test_prime_numbers():
    """Test known prime numbers."""
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for num in prime_numbers:
        assert is_prime(num) is True, f"{num} should be prime"

def test_non_prime_numbers():
    """Test known non-prime numbers."""
    non_prime_numbers = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15]
    for num in non_prime_numbers:
        assert is_prime(num) is False, f"{num} should not be prime"

def test_large_prime():
    """Test a large prime number."""
    assert is_prime(104729) is True

def test_large_non_prime():
    """Test a large non-prime number."""
    assert is_prime(104730) is False

def test_invalid_input_types():
    """Test that invalid input types raise a ValueError."""
    invalid_inputs = [
        "not a number", 
        3.14, 
        [2], 
        None
    ]
    
    for invalid_input in invalid_inputs:
        with pytest.raises(ValueError, match="Input must be an integer"):
            is_prime(invalid_input)

def test_negative_numbers():
    """Test that negative numbers are not prime."""
    negative_numbers = [-1, -2, -3, -5, -7]
    for num in negative_numbers:
        assert is_prime(num) is False