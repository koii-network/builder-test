import pytest
from src.gcd_calculator import gcd_with_prime_factors

def test_gcd_same_numbers():
    """Test GCD of same numbers"""
    assert gcd_with_prime_factors(10, 10) == 10
    assert gcd_with_prime_factors(7, 7) == 7

def test_gcd_basic_cases():
    """Test basic GCD calculations"""
    assert gcd_with_prime_factors(48, 18) == 6  # 2^4 * 3 vs 2 * 3^2
    assert gcd_with_prime_factors(54, 24) == 6  # 2 * 3^3 vs 2^3 * 3
    assert gcd_with_prime_factors(100, 75) == 25  # 2^2 * 5^2 vs 3 * 5^2

def test_gcd_coprime():
    """Test GCD of coprime numbers"""
    assert gcd_with_prime_factors(17, 23) == 1
    assert gcd_with_prime_factors(11, 13) == 1

def test_gcd_one_number_divisible():
    """Test GCD when one number is divisible by another"""
    assert gcd_with_prime_factors(36, 12) == 12
    assert gcd_with_prime_factors(100, 25) == 25

def test_gcd_prime_number_input():
    """Test GCD with prime number inputs"""
    assert gcd_with_prime_factors(11, 17) == 1
    assert gcd_with_prime_factors(7, 7) == 7

def test_invalid_input_type():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        gcd_with_prime_factors("10", 20)
    with pytest.raises(TypeError):
        gcd_with_prime_factors(10, "20")
    with pytest.raises(TypeError):
        gcd_with_prime_factors(10.5, 20)

def test_invalid_input_value():
    """Test error handling for invalid input values"""
    with pytest.raises(ValueError):
        gcd_with_prime_factors(0, 20)
    with pytest.raises(ValueError):
        gcd_with_prime_factors(10, 0)
    with pytest.raises(ValueError):
        gcd_with_prime_factors(-5, 20)
    with pytest.raises(ValueError):
        gcd_with_prime_factors(10, -5)