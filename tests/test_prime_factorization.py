import pytest
from src.prime_factorization import prime_factorization

def test_prime_factorization_basic():
    """Test basic prime factorization scenarios"""
    assert prime_factorization(12) == [2, 2, 3]
    assert prime_factorization(15) == [3, 5]
    assert prime_factorization(100) == [2, 2, 5, 5]

def test_prime_factorization_prime_numbers():
    """Test prime numbers"""
    assert prime_factorization(2) == [2]
    assert prime_factorization(17) == [17]
    assert prime_factorization(97) == [97]

def test_prime_factorization_edge_cases():
    """Test edge cases"""
    assert prime_factorization(0) == []
    assert prime_factorization(1) == []

def test_prime_factorization_large_number():
    """Test large number factorization"""
    result = prime_factorization(84672)
    # Verify the prime factorization without enforcing exact order
    assert all(isinstance(x, int) and x > 1 for x in result)
    assert prod(result) == 84672
    
    # Verify key characteristics of the factorization
    assert len(result) > 0

def prod(iterable):
    """Simple product function for testing"""
    result = 1
    for x in iterable:
        result *= x
    return result

def test_prime_factorization_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Input must be an integer"):
        prime_factorization("not an int")
    
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        prime_factorization(-5)

def test_prime_factorization_result_order():
    """Verify that factors are returned in ascending order"""
    result = prime_factorization(120)
    assert result == [2, 2, 2, 3, 5]