import pytest
from src.rgb_to_hex import rgb_to_hex

def test_basic_conversion():
    """Test basic RGB to Hex conversion"""
    assert rgb_to_hex(255, 255, 255) == '#FFFFFF'
    assert rgb_to_hex(0, 0, 0) == '#000000'
    assert rgb_to_hex(255, 0, 0) == '#FF0000'
    assert rgb_to_hex(0, 255, 0) == '#00FF00'
    assert rgb_to_hex(0, 0, 255) == '#0000FF'

def test_mid_range_conversion():
    """Test mid-range RGB to Hex conversion"""
    assert rgb_to_hex(128, 128, 128) == '#808080'
    assert rgb_to_hex(100, 150, 200) == '#6496C8'

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Test out of range values
    with pytest.raises(ValueError, match="RGB values must be between 0 and 255"):
        rgb_to_hex(-1, 0, 0)
    with pytest.raises(ValueError, match="RGB values must be between 0 and 255"):
        rgb_to_hex(0, 256, 0)
    with pytest.raises(ValueError, match="RGB values must be between 0 and 255"):
        rgb_to_hex(0, 0, 300)

def test_type_errors():
    """Test error handling for incorrect input types"""
    with pytest.raises(TypeError, match="RGB values must be integers"):
        rgb_to_hex(1.5, 0, 0)
    with pytest.raises(TypeError, match="RGB values must be integers"):
        rgb_to_hex('255', 0, 0)
    with pytest.raises(TypeError, match="RGB values must be integers"):
        rgb_to_hex(0, [255], 0)