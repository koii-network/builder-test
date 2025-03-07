import pytest
from src.unique_substrings import find_unique_substrings

def test_find_unique_substrings_normal_string():
    """Test finding unique substrings in a normal string"""
    result = find_unique_substrings("abcb")
    expected = ['a', 'ab', 'abc', 'abcb', 'b', 'bc', 'bcb', 'c', 'cb']
    assert sorted(result) == sorted(expected)

def test_find_unique_substrings_empty_string():
    """Test finding unique substrings in an empty string"""
    assert find_unique_substrings("") == []

def test_find_unique_substrings_single_char():
    """Test finding unique substrings in a single-character string"""
    result = find_unique_substrings("a")
    assert result == ['a']

def test_find_unique_substrings_repeated_chars():
    """Test finding unique substrings with repeated characters"""
    result = find_unique_substrings("aaaa")
    expected = ['a', 'aa', 'aaa', 'aaaa']
    assert sorted(result) == sorted(expected)

def test_find_unique_substrings_invalid_input():
    """Test that a TypeError is raised for non-string input"""
    with pytest.raises(TypeError, match="Input must be a string"):
        find_unique_substrings(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        find_unique_substrings(None)
    with pytest.raises(TypeError, match="Input must be a string"):
        find_unique_substrings(["abc"])