import pytest
from src.prime_number_checker import is_prime

def test_prime_numbers():
    # Test known prime numbers
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(13) == True
    assert is_prime(17) == True
    assert is_prime(19) == True

def test_non_prime_numbers():
    # Test known non-prime numbers
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
    assert is_prime(12) == False
    assert is_prime(15) == False

def test_large_prime():
    # Test a larger prime number
    assert is_prime(97) == True
    assert is_prime(101) == True

def test_large_non_prime():
    # Test a larger non-prime number
    assert is_prime(100) == False

def test_invalid_inputs():
    # Test error handling
    with pytest.raises(TypeError):
        is_prime("2")
    
    with pytest.raises(TypeError):
        is_prime(3.14)
    
    with pytest.raises(ValueError):
        is_prime(1)
    
    with pytest.raises(ValueError):
        is_prime(0)
    
    with pytest.raises(ValueError):
        is_prime(-5)