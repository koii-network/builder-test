import pytest
from src.rgb_to_hex import rgb_to_hex

def test_rgb_to_hex_basic():
    """Test basic color conversion"""
    assert rgb_to_hex(255, 128, 0) == 'FF8000'
    assert rgb_to_hex(0, 0, 0) == '000000'
    assert rgb_to_hex(255, 255, 255) == 'FFFFFF'

def test_rgb_to_hex_edge_cases():
    """Test edge case values"""
    assert rgb_to_hex(0, 0, 0) == '000000'
    assert rgb_to_hex(255, 255, 255) == 'FFFFFF'

def test_rgb_to_hex_lowercase_conversion():
    """Ensure output is always uppercase"""
    result = rgb_to_hex(10, 20, 30)
    assert result == result.upper()

def test_rgb_to_hex_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Test out of range values
    with pytest.raises(ValueError, match="Red value must be between 0 and 255"):
        rgb_to_hex(-1, 0, 0)
    
    with pytest.raises(ValueError, match="Green value must be between 0 and 255"):
        rgb_to_hex(0, 256, 0)
    
    with pytest.raises(ValueError, match="Blue value must be between 0 and 255"):
        rgb_to_hex(0, 0, 300)

def test_rgb_to_hex_type_errors():
    """Test type checking for inputs"""
    with pytest.raises(TypeError, match="Red value must be an integer"):
        rgb_to_hex('255', 0, 0)
    
    with pytest.raises(TypeError, match="Green value must be an integer"):
        rgb_to_hex(0, '128', 0)
    
    with pytest.raises(TypeError, match="Blue value must be an integer"):
        rgb_to_hex(0, 0, '64')