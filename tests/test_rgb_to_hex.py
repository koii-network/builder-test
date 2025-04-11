import pytest
from src.rgb_to_hex import rgb_to_hex

def test_basic_conversion():
    """Test standard RGB to hex conversion"""
    assert rgb_to_hex(255, 0, 0) == '#FF0000'  # Red
    assert rgb_to_hex(0, 255, 0) == '#00FF00'  # Green
    assert rgb_to_hex(0, 0, 255) == '#0000FF'  # Blue
    assert rgb_to_hex(128, 128, 128) == '#808080'  # Gray

def test_zero_values():
    """Test conversion with zero values"""
    assert rgb_to_hex(0, 0, 0) == '#000000'  # Black

def test_padding():
    """Test that single-digit hex values are padded"""
    assert rgb_to_hex(1, 2, 3) == '#010203'

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Values below 0
    with pytest.raises(ValueError, match="must be between 0 and 255"):
        rgb_to_hex(-1, 0, 0)
    with pytest.raises(ValueError, match="must be between 0 and 255"):
        rgb_to_hex(0, -1, 0)
    with pytest.raises(ValueError, match="must be between 0 and 255"):
        rgb_to_hex(0, 0, -1)

    # Values above 255
    with pytest.raises(ValueError, match="must be between 0 and 255"):
        rgb_to_hex(256, 0, 0)
    with pytest.raises(ValueError, match="must be between 0 and 255"):
        rgb_to_hex(0, 256, 0)
    with pytest.raises(ValueError, match="must be between 0 and 255"):
        rgb_to_hex(0, 0, 256)

def test_type_errors():
    """Test error handling for incorrect input types"""
    with pytest.raises(TypeError, match="Red must be an integer"):
        rgb_to_hex('255', 0, 0)
    with pytest.raises(TypeError, match="Green must be an integer"):
        rgb_to_hex(0, '255', 0)
    with pytest.raises(TypeError, match="Blue must be an integer"):
        rgb_to_hex(0, 0, '255')