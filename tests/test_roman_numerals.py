import pytest
from src.roman_numerals import to_roman_numeral

def test_basic_conversions():
    """Test basic integer to Roman numeral conversions"""
    assert to_roman_numeral(1) == 'I'
    assert to_roman_numeral(4) == 'IV'
    assert to_roman_numeral(9) == 'IX'
    assert to_roman_numeral(14) == 'XIV'
    assert to_roman_numeral(49) == 'XLIX'
    assert to_roman_numeral(99) == 'XCIX'
    assert to_roman_numeral(500) == 'D'
    assert to_roman_numeral(3999) == 'MMMCMXCIX'

def test_zero():
    """Test conversion of 0"""
    assert to_roman_numeral(0) == ''

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Input must be between 0 and 3999"):
        to_roman_numeral(-1)
    
    with pytest.raises(ValueError, match="Input must be between 0 and 3999"):
        to_roman_numeral(4000)

def test_type_error():
    """Test type checking"""
    with pytest.raises(TypeError, match="Input must be an integer"):
        to_roman_numeral("100")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        to_roman_numeral(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        to_roman_numeral(None)

def test_edge_cases():
    """Test edge cases and special numbers"""
    assert to_roman_numeral(1) == 'I'
    assert to_roman_numeral(3) == 'III'
    assert to_roman_numeral(4) == 'IV'
    assert to_roman_numeral(5) == 'V'
    assert to_roman_numeral(9) == 'IX'
    assert to_roman_numeral(10) == 'X'
    assert to_roman_numeral(40) == 'XL'
    assert to_roman_numeral(50) == 'L'
    assert to_roman_numeral(90) == 'XC'
    assert to_roman_numeral(100) == 'C'
    assert to_roman_numeral(400) == 'CD'
    assert to_roman_numeral(500) == 'D'
    assert to_roman_numeral(900) == 'CM'
    assert to_roman_numeral(1000) == 'M'