import pytest
from src.substring_extractor import extract_unique_substrings

def test_basic_substring_extraction():
    """Test basic substring extraction"""
    result = extract_unique_substrings("abc")
    expected = ['a', 'b', 'c', 'ab', 'bc', 'abc']
    assert sorted(result) == sorted(expected)

def test_empty_string():
    """Test extraction from empty string"""
    assert extract_unique_substrings("") == []

def test_single_character_string():
    """Test string with single character"""
    result = extract_unique_substrings("x")
    assert result == ['x']

def test_repeated_characters():
    """Test string with repeated characters"""
    result = extract_unique_substrings("aaaa")
    expected = ['a', 'aa', 'aaa', 'aaaa']
    assert sorted(result) == sorted(expected)

def test_invalid_input_type():
    """Test handling of non-string input"""
    with pytest.raises(TypeError, match="Input must be a string"):
        extract_unique_substrings(123)
        extract_unique_substrings(None)

def test_complex_string():
    """Test a more complex string"""
    result = extract_unique_substrings("hello")
    expected = ['h', 'e', 'l', 'o', 'he', 'el', 'll', 'lo', 'hel', 'ell', 'llo', 'hello']
    assert sorted(result) == sorted(expected)