import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindromes():
    """Test basic palindrome scenarios"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("A") == True
    assert is_palindrome("") == True

def test_case_insensitive_palindromes():
    """Test palindromes with mixed case"""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("RaCeCaR") == True

def test_non_palindromes():
    """Test strings that are not palindromes"""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_palindromes_with_punctuation():
    """Test palindromes with non-alphanumeric characters"""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_error_handling():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        is_palindrome(123)
    with pytest.raises(TypeError):
        is_palindrome(None)
    with pytest.raises(TypeError):
        is_palindrome(["not", "a", "string"])