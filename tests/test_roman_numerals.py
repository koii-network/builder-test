import pytest
from src.roman_numerals import int_to_roman

def test_int_to_roman_basic_conversions():
    assert int_to_roman(1) == "I"
    assert int_to_roman(4) == "IV"
    assert int_to_roman(9) == "IX"
    assert int_to_roman(14) == "XIV"
    assert int_to_roman(49) == "XLIX"
    assert int_to_roman(99) == "XCIX"
    assert int_to_roman(500) == "D"
    assert int_to_roman(3999) == "MMMCMXCIX"

def test_int_to_roman_zero():
    assert int_to_roman(0) == "N"

def test_int_to_roman_invalid_inputs():
    with pytest.raises(TypeError):
        int_to_roman("100")
    
    with pytest.raises(ValueError):
        int_to_roman(-1)
    
    with pytest.raises(ValueError):
        int_to_roman(4000)

def test_int_to_roman_edge_cases():
    # Test all decade and century transition points
    assert int_to_roman(9) == "IX"
    assert int_to_roman(40) == "XL"
    assert int_to_roman(90) == "XC"
    assert int_to_roman(400) == "CD"
    assert int_to_roman(900) == "CM"