import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindromes():
    """Test basic palindrome scenarios"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("A") == True

def test_non_palindromes():
    """Test strings that are not palindromes"""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_palindrome_with_spaces_and_punctuation():
    """Test palindromes with spaces and punctuation"""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_empty_string():
    """Test empty string"""
    assert is_palindrome("") == True

def test_case_insensitive():
    """Test case-insensitive palindrome checking"""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("RaCeCaR") == True

def test_invalid_input():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        is_palindrome(12345)
    with pytest.raises(TypeError):
        is_palindrome(None)
    with pytest.raises(TypeError):
        is_palindrome(["not", "a", "string"])