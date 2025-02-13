import pytest
from src.prime_checker import is_prime

def test_prime_numbers():
    # Test known prime numbers
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(13) == True

def test_non_prime_numbers():
    # Test known non-prime numbers
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False

def test_edge_cases():
    # Test edge cases
    assert is_prime(0) == False
    assert is_prime(-1) == False
    assert is_prime(-17) == False

def test_invalid_input():
    # Test invalid input types
    with pytest.raises(ValueError):
        is_prime(3.14)
    with pytest.raises(ValueError):
        is_prime("17")
    with pytest.raises(ValueError):
        is_prime(None)