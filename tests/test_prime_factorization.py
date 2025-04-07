import pytest
from src.prime_factorization import prime_factorization

def test_prime_factorization_basic():
    assert prime_factorization(12) == [2, 2, 3]
    assert prime_factorization(15) == [3, 5]
    assert prime_factorization(100) == [2, 2, 5, 5]

def test_prime_factorization_prime_numbers():
    assert prime_factorization(7) == [7]
    assert prime_factorization(13) == [13]
    assert prime_factorization(17) == [17]

def test_prime_factorization_edge_cases():
    assert prime_factorization(1) == []

def test_prime_factorization_large_number():
    assert prime_factorization(84) == [2, 2, 3, 7]

def test_prime_factorization_invalid_input():
    with pytest.raises(ValueError):
        prime_factorization(0)
    
    with pytest.raises(ValueError):
        prime_factorization(-5)
    
    with pytest.raises(ValueError):
        prime_factorization(3.14)
    
    with pytest.raises(ValueError):
        prime_factorization("not a number")