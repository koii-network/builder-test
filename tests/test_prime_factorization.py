import pytest
from src.prime_factorization import prime_factorization

def test_small_prime_number():
    assert prime_factorization(2) == [2]
    assert prime_factorization(3) == [3]
    assert prime_factorization(5) == [5]

def test_composite_numbers():
    assert prime_factorization(4) == [2, 2]
    assert prime_factorization(12) == [2, 2, 3]
    assert prime_factorization(100) == [2, 2, 5, 5]
    assert prime_factorization(84) == [2, 2, 3, 7]

def test_large_prime_number():
    assert prime_factorization(97) == [97]

def test_error_cases():
    with pytest.raises(ValueError, match="Input must be 2 or greater"):
        prime_factorization(1)
    
    with pytest.raises(ValueError, match="Input must be 2 or greater"):
        prime_factorization(0)
    
    with pytest.raises(ValueError, match="Input must be 2 or greater"):
        prime_factorization(-5)

def test_type_errors():
    with pytest.raises(TypeError, match="Input must be an integer"):
        prime_factorization(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        prime_factorization("12")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        prime_factorization(None)