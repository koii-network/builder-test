import pytest
from src.substring_finder import find_unique_substrings

def test_unique_substrings_basic():
    """Test basic substring finding."""
    result = find_unique_substrings("abc")
    assert result == ["a", "ab", "abc", "b", "bc", "c"]

def test_unique_substrings_repeated():
    """Test handling of strings with repeated characters."""
    result = find_unique_substrings("aaa")
    assert result == ["a", "aa", "aaa"]

def test_unique_substrings_empty():
    """Test handling of empty string."""
    result = find_unique_substrings("")
    assert result == []

def test_unique_substrings_single_char():
    """Test handling of single character string."""
    result = find_unique_substrings("x")
    assert result == ["x"]

def test_invalid_input():
    """Test handling of non-string input."""
    with pytest.raises(TypeError):
        find_unique_substrings(123)
    with pytest.raises(TypeError):
        find_unique_substrings(None)

def test_unique_substrings_complex():
    """Test a more complex string with varied characters."""
    result = find_unique_substrings("hello")
    expected = ["h", "he", "hel", "hell", "hello", 
                "e", "el", "ell", "ello", 
                "l", "ll", "llo", 
                "lo", 
                "o"]
    assert result == expected