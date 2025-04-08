import pytest
from src.lcm_calculator import lcm_with_gcd

def test_lcm_basic_cases():
    """Test basic LCM calculations."""
    assert lcm_with_gcd(4, 6) == 12
    assert lcm_with_gcd(15, 25) == 75
    assert lcm_with_gcd(12, 18) == 36

def test_lcm_prime_numbers():
    """Test LCM of prime numbers."""
    assert lcm_with_gcd(2, 3) == 6
    assert lcm_with_gcd(5, 7) == 35
    assert lcm_with_gcd(11, 13) == 143

def test_lcm_same_number():
    """Test LCM of the same number."""
    assert lcm_with_gcd(7, 7) == 7
    assert lcm_with_gcd(100, 100) == 100

def test_lcm_one_number_multiple():
    """Test LCM when one number is a multiple of the other."""
    assert lcm_with_gcd(4, 8) == 8
    assert lcm_with_gcd(3, 15) == 15

def test_lcm_large_numbers():
    """Test LCM of larger numbers."""
    assert lcm_with_gcd(48, 180) == 720
    assert lcm_with_gcd(64, 96) == 192

def test_lcm_invalid_inputs():
    """Test input validation."""
    # Test non-integer inputs
    with pytest.raises(TypeError):
        lcm_with_gcd(4.5, 6)
    with pytest.raises(TypeError):
        lcm_with_gcd("12", 15)
    
    # Test non-positive inputs
    with pytest.raises(ValueError):
        lcm_with_gcd(0, 5)
    with pytest.raises(ValueError):
        lcm_with_gcd(-4, 6)
    with pytest.raises(ValueError):
        lcm_with_gcd(4, -6)