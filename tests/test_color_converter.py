import pytest
from src.color_converter import rgb_to_hex

def test_basic_rgb_to_hex():
    """Test basic color conversion"""
    assert rgb_to_hex(255, 0, 0) == '#FF0000'  # Red
    assert rgb_to_hex(0, 255, 0) == '#00FF00'  # Green
    assert rgb_to_hex(0, 0, 255) == '#0000FF'  # Blue
    assert rgb_to_hex(255, 255, 255) == '#FFFFFF'  # White
    assert rgb_to_hex(0, 0, 0) == '#000000'  # Black

def test_float_inputs():
    """Test conversion with float inputs"""
    assert rgb_to_hex(255.0, 128.0, 0.0) == '#FF8000'
    assert rgb_to_hex(100.5, 200.7, 50.2) == '#64C832'

def test_edge_case_inputs():
    """Test edge case inputs"""
    assert rgb_to_hex(0, 0, 0) == '#000000'
    assert rgb_to_hex(255, 255, 255) == '#FFFFFF'

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Out of range values
    with pytest.raises(ValueError, match="RGB values must be between 0 and 255"):
        rgb_to_hex(256, 0, 0)
    with pytest.raises(ValueError, match="RGB values must be between 0 and 255"):
        rgb_to_hex(0, -1, 0)
    
    # Non-numeric inputs
    with pytest.raises(TypeError, match="RGB values must be numeric"):
        rgb_to_hex('red', 0, 0)
    with pytest.raises(TypeError, match="RGB values must be numeric"):
        rgb_to_hex(0, [1], 0)
    
    # Non-convertible inputs
    with pytest.raises(TypeError, match="RGB values must be convertible to integers"):
        rgb_to_hex(255.5, '100', 0)