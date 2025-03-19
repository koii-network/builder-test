import pytest
from src.substring_finder import find_unique_substrings

def test_find_unique_substrings_basic():
    """Test basic substring finding functionality."""
    result = find_unique_substrings("abc")
    expected = ['a', 'ab', 'abc', 'b', 'bc', 'c']
    assert sorted(result) == expected

def test_find_unique_substrings_empty_string():
    """Test with an empty string."""
    assert find_unique_substrings("") == []

def test_find_unique_substrings_single_char():
    """Test with a single character string."""
    result = find_unique_substrings("a")
    assert result == ['a']

def test_find_unique_substrings_repeated_chars():
    """Test with repeated characters."""
    result = find_unique_substrings("aaa")
    expected = ['a', 'aa', 'aaa']
    assert sorted(result) == expected

def test_find_unique_substrings_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        find_unique_substrings(123)
    
    with pytest.raises(TypeError):
        find_unique_substrings(None)

def test_find_unique_substrings_whitespace():
    """Test handling of strings with whitespace."""
    result = find_unique_substrings(" a b ")
    expected = [' ', ' a', ' a ', ' b', ' b ', 'a', 'a ', 'b', 'b ']
    assert sorted(result) == expected

def test_find_unique_substrings_mixed_chars():
    """Test with a mix of characters."""
    result = find_unique_substrings("hello")
    expected = ['e', 'el', 'ell', 'ello', 'h', 'he', 'hel', 'hell', 'hello', 'l', 'll', 'llo', 'lo', 'o']
    assert sorted(result) == expected