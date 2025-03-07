import pytest
from src.roman_numerals import convert_to_roman

def test_convert_to_roman_basic_numbers():
    """Test conversion of basic numbers"""
    assert convert_to_roman(1) == 'I'
    assert convert_to_roman(4) == 'IV'
    assert convert_to_roman(5) == 'V'
    assert convert_to_roman(9) == 'IX'
    assert convert_to_roman(10) == 'X'
    assert convert_to_roman(14) == 'XIV'
    assert convert_to_roman(40) == 'XL'
    assert convert_to_roman(49) == 'XLIX'
    assert convert_to_roman(50) == 'L'
    assert convert_to_roman(90) == 'XC'
    assert convert_to_roman(99) == 'XCIX'
    assert convert_to_roman(100) == 'C'
    assert convert_to_roman(400) == 'CD'
    assert convert_to_roman(500) == 'D'
    assert convert_to_roman(900) == 'CM'
    assert convert_to_roman(1000) == 'M'

def test_convert_to_roman_large_numbers():
    """Test conversion of larger numbers"""
    assert convert_to_roman(3999) == 'MMMCMXCIX'
    assert convert_to_roman(2023) == 'MMXXIII'
    assert convert_to_roman(1984) == 'MCMLXXXIV'

def test_convert_to_roman_zero():
    """Test conversion of zero"""
    assert convert_to_roman(0) == ''

def test_convert_to_roman_invalid_inputs():
    """Test invalid input handling"""
    with pytest.raises(TypeError, match="Input must be an integer"):
        convert_to_roman('10')
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        convert_to_roman(3.14)
    
    with pytest.raises(ValueError, match="Input must be between 0 and 3999"):
        convert_to_roman(-1)
    
    with pytest.raises(ValueError, match="Input must be between 0 and 3999"):
        convert_to_roman(4000)