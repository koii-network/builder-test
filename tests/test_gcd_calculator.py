import pytest
from src.gcd_calculator import gcd_using_prime_factors

def test_gcd_using_prime_factors_basic():
    """Test basic GCD calculations"""
    assert gcd_using_prime_factors(48, 18) == 6
    assert gcd_using_prime_factors(54, 24) == 6
    assert gcd_using_prime_factors(17, 23) == 1
    assert gcd_using_prime_factors(100, 75) == 25

def test_gcd_using_prime_factors_same_number():
    """Test GCD when both numbers are the same"""
    assert gcd_using_prime_factors(7, 7) == 7
    assert gcd_using_prime_factors(100, 100) == 100

def test_gcd_using_prime_factors_one_is_multiple():
    """Test GCD when one number is a multiple of the other"""
    assert gcd_using_prime_factors(12, 36) == 12
    assert gcd_using_prime_factors(36, 12) == 12

def test_gcd_using_prime_factors_coprime():
    """Test GCD of coprime numbers"""
    assert gcd_using_prime_factors(17, 22) == 1
    assert gcd_using_prime_factors(13, 16) == 1

def test_gcd_using_prime_factors_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        gcd_using_prime_factors(0, 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        gcd_using_prime_factors(-5, 10)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        gcd_using_prime_factors(5, 0)