import pytest
import sys
import os

# Add the repository root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.string_reverser import reverse_string

def test_basic_string_reversal():
    """Test basic string reversal"""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"

def test_empty_string():
    """Test empty string reversal"""
    assert reverse_string("") == ""

def test_single_character():
    """Test single character string"""
    assert reverse_string("a") == "a"

def test_palindrome():
    """Test palindrome reversal"""
    assert reverse_string("racecar") == "racecar"

def test_string_with_special_characters():
    """Test string with special characters"""
    assert reverse_string("hello, world!") == "!dlrow ,olleh"

def test_string_with_numbers():
    """Test string with numbers"""
    assert reverse_string("h3llo123") == "321oll3h"

def test_non_string_input():
    """Test non-string input raises TypeError"""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(12345)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(["list"])