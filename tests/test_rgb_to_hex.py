import pytest
from src.rgb_to_hex import rgb_to_hex

def test_basic_conversion():
    """Test basic RGB to hex conversion"""
    assert rgb_to_hex(255, 0, 0) == 'FF0000'  # Red
    assert rgb_to_hex(0, 255, 0) == '00FF00'  # Green
    assert rgb_to_hex(0, 0, 255) == '0000FF'  # Blue
    assert rgb_to_hex(255, 255, 255) == 'FFFFFF'  # White
    assert rgb_to_hex(0, 0, 0) == '000000'  # Black

def test_mixed_colors():
    """Test mixed color conversions"""
    assert rgb_to_hex(128, 128, 128) == '808080'  # Gray
    assert rgb_to_hex(255, 165, 0) == 'FFA500'   # Orange

def test_edge_cases():
    """Test edge cases at 0 and 255"""
    assert rgb_to_hex(0, 0, 0) == '000000'
    assert rgb_to_hex(255, 255, 255) == 'FFFFFF'

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        rgb_to_hex('255', 0, 0)
    with pytest.raises(TypeError):
        rgb_to_hex(255, '0', 0)
    with pytest.raises(TypeError):
        rgb_to_hex(255, 0, '0')

def test_out_of_range_values():
    """Test error handling for out-of-range values"""
    with pytest.raises(ValueError):
        rgb_to_hex(-1, 0, 0)
    with pytest.raises(ValueError):
        rgb_to_hex(0, 256, 0)
    with pytest.raises(ValueError):
        rgb_to_hex(0, 0, 300)