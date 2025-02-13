import pytest
from src.string_utils import reverse_string

def test_reverse_string_basic():
    """Test basic string reversal."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"

def test_reverse_string_empty():
    """Test reversing an empty string."""
    assert reverse_string("") == ""

def test_reverse_string_special_chars():
    """Test reversing strings with special characters."""
    assert reverse_string("a1b2c3") == "3c2b1a"
    assert reverse_string("Hello, World!") == "!dlroW ,olleH"

def test_reverse_string_unicode():
    """Test reversing unicode strings."""
    assert reverse_string("café") == "éfac"

def test_reverse_string_invalid_input():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError):
        reverse_string(123)
    
    with pytest.raises(TypeError):
        reverse_string(None)
    
    with pytest.raises(TypeError):
        reverse_string(["hello"])