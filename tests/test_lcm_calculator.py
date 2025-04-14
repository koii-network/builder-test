import pytest
from src.lcm_calculator import lcm, lcm_multiple

def test_lcm_basic_functionality():
    """Test basic LCM calculations"""
    assert lcm(4, 6) == 12
    assert lcm(21, 6) == 42
    assert lcm(17, 5) == 85

def test_lcm_same_number():
    """Test LCM when both numbers are the same"""
    assert lcm(7, 7) == 7
    assert lcm(13, 13) == 13

def test_lcm_one_is_multiple():
    """Test LCM when one number is a multiple of the other"""
    assert lcm(8, 4) == 8
    assert lcm(15, 5) == 15

def test_lcm_coprime():
    """Test LCM of coprime numbers"""
    assert lcm(7, 11) == 77
    assert lcm(13, 17) == 221

def test_lcm_multiple_integers():
    """Test LCM calculation with multiple integers"""
    assert lcm_multiple(2, 3, 4) == 12
    assert lcm_multiple(3, 4, 6) == 12
    assert lcm_multiple(2, 3, 5, 7) == 210

def test_lcm_error_handling():
    """Test error handling for invalid inputs"""
    # Test non-integer inputs
    with pytest.raises(TypeError):
        lcm(4.5, 6)
    with pytest.raises(TypeError):
        lcm("4", 6)
    
    # Test non-positive integer inputs
    with pytest.raises(ValueError):
        lcm(0, 6)
    with pytest.raises(ValueError):
        lcm(-4, 6)
    
    # Test multiple LCM with no arguments or invalid inputs
    with pytest.raises(ValueError):
        lcm_multiple()
    with pytest.raises(TypeError):
        lcm_multiple(2, 3, "4")
    with pytest.raises(ValueError):
        lcm_multiple(0, 3, 4)