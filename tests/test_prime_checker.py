import pytest
from src.prime_checker import is_prime

def test_prime_numbers():
    """Test known prime numbers."""
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for num in prime_numbers:
        assert is_prime(num) == True, f"{num} should be prime"

def test_non_prime_numbers():
    """Test known non-prime numbers."""
    non_prime_numbers = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15]
    for num in non_prime_numbers:
        assert is_prime(num) == False, f"{num} should not be prime"

def test_large_prime():
    """Test a large prime number."""
    assert is_prime(104729) == True, "Large prime number check failed"

def test_large_non_prime():
    """Test a large non-prime number."""
    assert is_prime(104730) == False, "Large non-prime number check failed"

def test_float_inputs():
    """Test float inputs."""
    assert is_prime(7.0) == True, "Integer-like float should be prime"
    assert is_prime(4.0) == False, "Integer-like non-prime float should not be prime"
    assert is_prime(3.5) == False, "Non-integer float should not be prime"

def test_negative_numbers():
    """Test negative number inputs."""
    assert is_prime(-7) == False, "Negative numbers should not be prime"
    assert is_prime(-2) == False, "Negative numbers should not be prime"

def test_invalid_inputs():
    """Test invalid input types."""
    with pytest.raises(TypeError):
        is_prime("7")
    with pytest.raises(TypeError):
        is_prime([7])
    with pytest.raises(TypeError):
        is_prime(None)