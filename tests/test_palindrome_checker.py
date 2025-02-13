import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindromes():
    """Test basic palindrome scenarios"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("deified") == True

def test_non_palindromes():
    """Test non-palindrome scenarios"""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_case_insensitive():
    """Test that palindrome check is case-insensitive"""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("Level") == True

def test_with_spaces_and_punctuation():
    """Test palindromes with spaces and punctuation"""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_empty_and_single_char():
    """Test empty string and single character"""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_numeric_palindromes():
    """Test numeric palindromes"""
    assert is_palindrome("12321") == True
    assert is_palindrome("123") == False

def test_mixed_character_palindromes():
    """Test palindromes with mixed alphanumeric characters"""
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b2c3b1a") == False