import pytest
from src.roman_numerals import to_roman_numeral

def test_basic_conversions():
    """Test basic conversions of numbers to Roman numerals"""
    assert to_roman_numeral(1) == 'I'
    assert to_roman_numeral(4) == 'IV'
    assert to_roman_numeral(9) == 'IX'
    assert to_roman_numeral(49) == 'XLIX'
    assert to_roman_numeral(99) == 'XCIX'
    assert to_roman_numeral(500) == 'D'
    assert to_roman_numeral(3999) == 'MMMCMXCIX'

def test_zero():
    """Test conversion of zero"""
    assert to_roman_numeral(0) == ''

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Test negative numbers
    with pytest.raises(ValueError, match="Input must be between 0 and 3999"):
        to_roman_numeral(-1)
    
    # Test numbers above max
    with pytest.raises(ValueError, match="Input must be between 0 and 3999"):
        to_roman_numeral(4000)
    
    # Test non-integer inputs
    with pytest.raises(TypeError, match="Input must be an integer"):
        to_roman_numeral(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        to_roman_numeral("42")

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