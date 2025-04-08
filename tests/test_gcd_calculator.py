import pytest
from src.gcd_calculator import gcd_using_prime_factors

def test_gcd_basic_cases():
    """Test basic GCD calculations."""
    assert gcd_using_prime_factors(48, 18) == 6
    assert gcd_using_prime_factors(54, 24) == 6
    assert gcd_using_prime_factors(17, 23) == 1
    assert gcd_using_prime_factors(100, 75) == 25

def test_gcd_zero_cases():
    """Test GCD calculations involving zero."""
    assert gcd_using_prime_factors(0, 5) == 5
    assert gcd_using_prime_factors(7, 0) == 7
    assert gcd_using_prime_factors(0, 0) == 0

def test_gcd_same_number():
    """Test GCD of a number with itself."""
    assert gcd_using_prime_factors(7, 7) == 7
    assert gcd_using_prime_factors(100, 100) == 100

def test_gcd_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Inputs must be integers"):
        gcd_using_prime_factors("10", 5)
    
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        gcd_using_prime_factors(-5, 10)
    
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        gcd_using_prime_factors(0, -5)

def test_gcd_large_numbers():
    """Test GCD calculations with larger numbers."""
    assert gcd_using_prime_factors(1024, 512) == 512
    assert gcd_using_prime_factors(2**10, 2**15) == 2**10
    assert gcd_using_prime_factors(15487469, 32451899) == 1  # Both prime