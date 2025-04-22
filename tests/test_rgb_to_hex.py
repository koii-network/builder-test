import pytest
from src.rgb_to_hex import rgb_to_hex

def test_rgb_to_hex_basic():
    """Test basic color conversion"""
    assert rgb_to_hex(255, 0, 0) == '#FF0000'  # Red
    assert rgb_to_hex(0, 255, 0) == '#00FF00'  # Green
    assert rgb_to_hex(0, 0, 255) == '#0000FF'  # Blue
    assert rgb_to_hex(255, 255, 255) == '#FFFFFF'  # White
    assert rgb_to_hex(0, 0, 0) == '#000000'  # Black

def test_rgb_to_hex_mixed_colors():
    """Test mixed color conversions"""
    assert rgb_to_hex(128, 128, 128) == '#808080'  # Gray
    assert rgb_to_hex(255, 165, 0) == '#FFA500'  # Orange

def test_rgb_to_hex_boundary_values():
    """Test boundary values"""
    assert rgb_to_hex(0, 0, 0) == '#000000'
    assert rgb_to_hex(255, 255, 255) == '#FFFFFF'

def test_rgb_to_hex_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Test negative values
    with pytest.raises(ValueError, match="Red value must be between 0 and 255"):
        rgb_to_hex(-1, 0, 0)
    
    with pytest.raises(ValueError, match="Green value must be between 0 and 255"):
        rgb_to_hex(0, -1, 0)
    
    with pytest.raises(ValueError, match="Blue value must be between 0 and 255"):
        rgb_to_hex(0, 0, -1)
    
    # Test values over 255
    with pytest.raises(ValueError, match="Red value must be between 0 and 255"):
        rgb_to_hex(256, 0, 0)
    
    with pytest.raises(ValueError, match="Green value must be between 0 and 255"):
        rgb_to_hex(0, 256, 0)
    
    with pytest.raises(ValueError, match="Blue value must be between 0 and 255"):
        rgb_to_hex(0, 0, 256)

def test_rgb_to_hex_type_errors():
    """Test type checking"""
    with pytest.raises(TypeError, match="Red value must be an integer"):
        rgb_to_hex('255', 0, 0)
    
    with pytest.raises(TypeError, match="Green value must be an integer"):
        rgb_to_hex(0, '255', 0)
    
    with pytest.raises(TypeError, match="Blue value must be an integer"):
        rgb_to_hex(0, 0, '255')