import pytest
from src.string_reverser import reverse_string

def test_reverse_basic_string():
    """Test reversing a basic string."""
    assert reverse_string("hello") == "olleh"

def test_reverse_empty_string():
    """Test reversing an empty string."""
    assert reverse_string("") == ""

def test_reverse_single_character():
    """Test reversing a single character string."""
    assert reverse_string("a") == "a"

def test_reverse_palindrome():
    """Test reversing a palindrome string."""
    assert reverse_string("racecar") == "racecar"

def test_reverse_with_spaces():
    """Test reversing a string with spaces."""
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_with_special_characters():
    """Test reversing a string with special characters."""
    assert reverse_string("Hello, World!") == "!dlroW ,olleH"

def test_raise_type_error_for_non_string():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(None)

    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(["hello"])