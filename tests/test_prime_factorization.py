import pytest
from src.prime_factorization import prime_factorization
from src.prime_utils import is_prime

def test_prime_factorization_basic():
    assert prime_factorization(12) == {2: 2, 3: 1}
    assert prime_factorization(15) == {3: 1, 5: 1}
    assert prime_factorization(100) == {2: 2, 5: 2}

def test_prime_factorization_prime_numbers():
    assert prime_factorization(7) == {7: 1}
    assert prime_factorization(13) == {13: 1}
    assert prime_factorization(17) == {17: 1}

def test_prime_factorization_edge_cases():
    assert prime_factorization(1) == {}

def test_prime_factorization_large_number():
    assert prime_factorization(84) == {2: 2, 3: 1, 7: 1}

def test_prime_factorization_invalid_input():
    with pytest.raises(ValueError):
        prime_factorization(0)
    
    with pytest.raises(ValueError):
        prime_factorization(-5)
    
    with pytest.raises(ValueError):
        prime_factorization(3.14)
    
    with pytest.raises(ValueError):
        prime_factorization("not a number")

def test_prime_factors_are_prime():
    """
    Verify that all factored components are prime.
    """
    test_cases = [12, 15, 100, 7, 13, 17, 84]
    
    for num in test_cases:
        factors = prime_factorization(num)
        # Check that all keys (prime factors) are indeed prime
        for factor in factors.keys():
            assert is_prime(factor), f"{factor} should be prime"