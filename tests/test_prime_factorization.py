import pytest
from src.prime_factorization import prime_factorization

def test_prime_factorization_basic():
    """Test basic prime factorization scenarios."""
    assert prime_factorization(2) == [2]
    assert prime_factorization(4) == [2, 2]
    assert prime_factorization(12) == [2, 2, 3]
    assert prime_factorization(15) == [3, 5]
    assert prime_factorization(100) == [2, 2, 5, 5]

def test_prime_factorization_large_number():
    """Test prime factorization for larger numbers."""
    assert prime_factorization(84) == [2, 2, 3, 7]
    assert prime_factorization(7919) == [7919]  # Prime number
    assert prime_factorization(7920) == [2, 2, 2, 2, 3, 3, 5, 11]

def test_prime_factorization_edge_cases():
    """Test edge cases and error handling."""
    with pytest.raises(ValueError, match="Input must be greater than or equal to 2"):
        prime_factorization(1)
    
    with pytest.raises(ValueError, match="Input must be greater than or equal to 2"):
        prime_factorization(0)
    
    with pytest.raises(ValueError, match="Input must be greater than or equal to 2"):
        prime_factorization(-5)

def test_prime_factorization_type_errors():
    """Test type error handling."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        prime_factorization(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        prime_factorization("12")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        prime_factorization(None)