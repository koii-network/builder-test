import pytest
from src.color_converter import rgb_to_hex

def test_rgb_to_hex_individual_values():
    """Test conversion with individual RGB values"""
    assert rgb_to_hex(255, 0, 0) == '#FF0000'
    assert rgb_to_hex(0, 255, 0) == '#00FF00'
    assert rgb_to_hex(0, 0, 255) == '#0000FF'

def test_rgb_to_hex_tuple():
    """Test conversion with RGB tuple"""
    assert rgb_to_hex((255, 0, 0)) == '#FF0000'
    assert rgb_to_hex((0, 255, 0)) == '#00FF00'
    assert rgb_to_hex((0, 0, 255)) == '#0000FF'

def test_rgb_to_hex_mixed_colors():
    """Test conversion with mixed RGB values"""
    assert rgb_to_hex(128, 128, 128) == '#808080'
    assert rgb_to_hex(255, 165, 0) == '#FFA500'

def test_rgb_to_hex_edge_cases():
    """Test edge case values"""
    assert rgb_to_hex(0, 0, 0) == '#000000'
    assert rgb_to_hex(255, 255, 255) == '#FFFFFF'

def test_rgb_to_hex_invalid_input():
    """Test error handling for invalid inputs"""
    # Too few arguments
    with pytest.raises(ValueError):
        rgb_to_hex(255, 0)
    
    # Too many arguments
    with pytest.raises(ValueError):
        rgb_to_hex(255, 0, 0, 0)
    
    # Non-integer values
    with pytest.raises(ValueError):
        rgb_to_hex(255.5, 0, 0)
    
    # Out of range values
    with pytest.raises(ValueError):
        rgb_to_hex(256, 0, 0)
    
    # Negative values
    with pytest.raises(ValueError):
        rgb_to_hex(-1, 0, 0)
    
    # Invalid input type
    with pytest.raises(ValueError):
        rgb_to_hex("255", "0", "0")
    
    # Invalid tuple/list
    with pytest.raises(ValueError):
        rgb_to_hex([255, 0])