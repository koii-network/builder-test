import pytest
from src.prime_factorization import prime_factorization

def test_prime_factorization_basic():
    """Test basic prime factorization"""
    assert prime_factorization(12) == [2, 2, 3]
    assert prime_factorization(15) == [3, 5]
    assert prime_factorization(100) == [2, 2, 5, 5]

def test_prime_factorization_prime_number():
    """Test prime factorization of prime numbers"""
    assert prime_factorization(7) == [7]
    assert prime_factorization(11) == [11]
    assert prime_factorization(17) == [17]

def test_prime_factorization_special_cases():
    """Test special cases"""
    assert prime_factorization(1) == []
    assert prime_factorization(2) == [2]

def test_prime_factorization_large_number():
    """Test prime factorization of a larger number"""
    assert prime_factorization(84) == [2, 2, 3, 7]

def test_prime_factorization_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Input must be an integer"):
        prime_factorization("12")
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(-5)

def test_prime_factorization_large_prime():
    """Test prime factorization of a large prime number"""
    large_prime = 104729  # A large prime number
    assert prime_factorization(large_prime) == [104729]