import pytest
from src.string_reversal import reverse_string

def test_reverse_string_basic():
    """Test basic string reversal."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"

def test_reverse_string_empty():
    """Test reversal of an empty string."""
    assert reverse_string("") == ""

def test_reverse_string_single_char():
    """Test reversal of a single character."""
    assert reverse_string("a") == "a"

def test_reverse_string_with_spaces():
    """Test reversal of string with spaces."""
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_string_with_punctuation():
    """Test reversal of string with punctuation."""
    assert reverse_string("hello, world!") == "!dlrow ,olleh"

def test_reverse_string_with_mixed_characters():
    """Test reversal of string with mixed character types."""
    assert reverse_string("a1b2c3") == "3c2b1a"

def test_reverse_string_unicode():
    """Test reversal of string with unicode characters."""
    assert reverse_string("café") == "éfac"

def test_reverse_string_invalid_input():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(["hello"]))