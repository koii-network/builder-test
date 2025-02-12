import pytest
from src.string_reversal import reverse_string

def test_reverse_basic_string():
    """Test reversing a basic string."""
    assert reverse_string("hello") == "olleh"

def test_reverse_empty_string():
    """Test reversing an empty string."""
    assert reverse_string("") == ""

def test_reverse_single_char():
    """Test reversing a single character."""
    assert reverse_string("a") == "a"

def test_reverse_with_spaces():
    """Test reversing a string with spaces."""
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_with_special_chars():
    """Test reversing a string with special characters."""
    assert reverse_string("a1b2c3!@#") == "#@!3c2b1a"

def test_reverse_non_string_raises_error():
    """Test that non-string input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(["list"])