import pytest
from src.string_reversal import reverse_string

def test_reverse_string_normal():
    """Test reversing a normal string."""
    assert reverse_string("hello") == "olleh"

def test_reverse_string_empty():
    """Test reversing an empty string."""
    assert reverse_string("") == ""

def test_reverse_string_single_char():
    """Test reversing a single character string."""
    assert reverse_string("a") == "a"

def test_reverse_string_with_spaces():
    """Test reversing a string with spaces."""
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_string_with_numbers():
    """Test reversing a string with numbers."""
    assert reverse_string("h3ll0") == "0ll3h"

def test_reverse_string_with_symbols():
    """Test reversing a string with symbols."""
    assert reverse_string("h@llo!") == "!oll@h"

def test_reverse_string_invalid_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(None)