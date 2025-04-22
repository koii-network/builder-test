import pytest
from src.rgb_to_hex import rgb_to_hex

def test_rgb_to_hex_basic():
    """Test basic color conversion"""
    assert rgb_to_hex(255, 255, 255) == 'FFFFFF'
    assert rgb_to_hex(0, 0, 0) == '000000'
    assert rgb_to_hex(148, 0, 211) == '9400D3'

def test_rgb_to_hex_edge_cases():
    """Test edge cases of color values"""
    assert rgb_to_hex(0, 0, 0) == '000000'
    assert rgb_to_hex(255, 255, 255) == 'FFFFFF'

def test_rgb_to_hex_single_digit_values():
    """Test conversion of single-digit values"""
    assert rgb_to_hex(4, 8, 15) == '04080F'

def test_rgb_to_hex_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Test values outside 0-255 range
    with pytest.raises(ValueError, match="Red value must be between 0 and 255"):
        rgb_to_hex(-1, 0, 0)
    
    with pytest.raises(ValueError, match="Green value must be between 0 and 255"):
        rgb_to_hex(0, 256, 0)
    
    with pytest.raises(ValueError, match="Blue value must be between 0 and 255"):
        rgb_to_hex(0, 0, 300)

def test_rgb_to_hex_non_integer_inputs():
    """Test error handling for non-integer inputs"""
    with pytest.raises(TypeError, match="Red value must be an integer"):
        rgb_to_hex('255', 0, 0)
    
    with pytest.raises(TypeError, match="Green value must be an integer"):
        rgb_to_hex(0, '255', 0)
    
    with pytest.raises(TypeError, match="Blue value must be an integer"):
        rgb_to_hex(0, 0, '255')