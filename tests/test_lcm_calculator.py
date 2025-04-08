import pytest
from src.lcm_calculator import lcm, lcm_multiple

def test_lcm_basic():
    """Test basic LCM calculations"""
    assert lcm(4, 6) == 12
    assert lcm(21, 6) == 42
    assert lcm(17, 5) == 85

def test_lcm_with_one():
    """Test LCM when one number is 1"""
    assert lcm(1, 5) == 5
    assert lcm(5, 1) == 5

def test_lcm_same_number():
    """Test LCM when both numbers are the same"""
    assert lcm(7, 7) == 7
    assert lcm(13, 13) == 13

def test_lcm_coprime():
    """Test LCM of coprime numbers"""
    assert lcm(17, 23) == 391
    assert lcm(11, 13) == 143

def test_lcm_multiple_numbers():
    """Test LCM of multiple numbers"""
    assert lcm_multiple(2, 3, 4) == 12
    assert lcm_multiple(3, 4, 6) == 12
    assert lcm_multiple(2, 3, 5, 7) == 210

def test_lcm_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Both inputs must be integers"):
        lcm(3.5, 4)
    
    with pytest.raises(ValueError, match="Both inputs must be positive integers"):
        lcm(-4, 6)
    
    with pytest.raises(ValueError, match="Both inputs must be positive integers"):
        lcm(4, 0)

def test_lcm_multiple_invalid_inputs():
    """Test error handling for lcm_multiple"""
    with pytest.raises(ValueError, match="At least one number must be provided"):
        lcm_multiple()
    
    with pytest.raises(ValueError, match="All inputs must be positive integers"):
        lcm_multiple(2, 3, 0)
    
    with pytest.raises(ValueError, match="All inputs must be positive integers"):
        lcm_multiple(2, -3, 4)
    
    with pytest.raises(ValueError, match="All inputs must be integers"):
        lcm_multiple(2, 3, 3.5)