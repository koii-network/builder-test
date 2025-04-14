import pytest
from src.gcd_calculator import gcd_using_prime_factors

def test_gcd_basic_cases():
    """Test basic GCD calculations."""
    assert gcd_using_prime_factors(48, 18) == 6
    assert gcd_using_prime_factors(54, 24) == 6
    assert gcd_using_prime_factors(100, 75) == 25

def test_gcd_coprime_numbers():
    """Test GCD of coprime numbers."""
    assert gcd_using_prime_factors(7, 13) == 1
    assert gcd_using_prime_factors(11, 17) == 1

def test_gcd_same_number():
    """Test GCD when both numbers are the same."""
    assert gcd_using_prime_factors(12, 12) == 12
    assert gcd_using_prime_factors(17, 17) == 17

def test_gcd_one_is_multiple():
    """Test GCD when one number is a multiple of the other."""
    assert gcd_using_prime_factors(24, 8) == 8
    assert gcd_using_prime_factors(8, 24) == 8

def test_gcd_one_is_one():
    """Test GCD when one number is 1."""
    assert gcd_using_prime_factors(1, 15) == 1
    assert gcd_using_prime_factors(15, 1) == 1

def test_gcd_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Inputs must be integers"):
        gcd_using_prime_factors(10.5, 15)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        gcd_using_prime_factors(0, 15)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        gcd_using_prime_factors(10, -5)

def test_gcd_large_numbers():
    """Test GCD calculation for larger numbers."""
    assert gcd_using_prime_factors(1260, 1680) == 420
    assert gcd_using_prime_factors(123456, 789012) == 12