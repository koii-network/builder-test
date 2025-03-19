import pytest
from src.substring_extractor import extract_unique_substrings

def test_normal_string():
    """Test extraction of unique substrings from a normal string."""
    result = extract_unique_substrings("abc")
    assert set(result) == set(['a', 'b', 'c', 'ab', 'bc', 'abc'])
    assert len(result) == 6

def test_empty_string():
    """Test extraction from an empty string."""
    result = extract_unique_substrings("")
    assert result == []

def test_repeated_characters():
    """Test string with repeated characters."""
    result = extract_unique_substrings("aaaa")
    assert set(result) == set(['a', 'aa', 'aaa', 'aaaa'])
    assert len(result) == 4

def test_single_character():
    """Test single character string."""
    result = extract_unique_substrings("x")
    assert result == ['x']

def test_error_non_string():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        extract_unique_substrings(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        extract_unique_substrings(None)

def test_complex_string():
    """Test a more complex string with mixed characters."""
    result = extract_unique_substrings("hello")
    expected = set(['h', 'e', 'l', 'o', 'he', 'el', 'll', 'lo', 'hel', 'ell', 'llo', 'hell', 'ello', 'hello'])
    assert set(result) == expected
    assert len(result) == 14