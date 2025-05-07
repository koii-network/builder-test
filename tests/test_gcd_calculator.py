import pytest
from src.gcd_calculator import gcd_prime_factors, prime_factorization

def test_prime_factorization():
    # Test basic prime factorization
    assert prime_factorization(12) == {2: 2, 3: 1}
    assert prime_factorization(100) == {2: 2, 5: 2}
    
    # Test edge cases
    assert prime_factorization(0) == {}
    assert prime_factorization(1) == {1: 1}
    assert prime_factorization(17) == {17: 1}  # Prime number

def test_gcd_prime_factors():
    # Basic GCD tests
    assert gcd_prime_factors(12, 18) == 6
    assert gcd_prime_factors(48, 18) == 6
    assert gcd_prime_factors(54, 24) == 6
    
    # Multiple numbers
    assert gcd_prime_factors(12, 18, 24) == 6
    
    # Single number
    assert gcd_prime_factors(42) == 42
    
    # Zero handling
    assert gcd_prime_factors(0, 5) == 5
    assert gcd_prime_factors(0, 0) == 0

def test_gcd_negative_numbers():
    # Negative number handling
    assert gcd_prime_factors(-12, 18) == 6
    assert gcd_prime_factors(12, -18) == 6
    assert gcd_prime_factors(-12, -18) == 6

def test_gcd_error_handling():
    # Error cases
    with pytest.raises(ValueError, match="At least one number must be provided"):
        gcd_prime_factors()
    
    with pytest.raises(TypeError, match="All arguments must be integers"):
        gcd_prime_factors(12, "18")
    
    with pytest.raises(TypeError, match="All arguments must be integers"):
        gcd_prime_factors(12, 3.14)

def test_prime_factorization_error_handling():
    # Negative number error
    with pytest.raises(ValueError, match="Cannot factorize negative numbers"):
        prime_factorization(-5)

def test_large_numbers():
    # Test with relatively large numbers
    assert gcd_prime_factors(1000000, 1000) == 1000
    assert gcd_prime_factors(1234567, 7654321) == 1