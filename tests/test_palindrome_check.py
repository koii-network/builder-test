import pytest
from src.palindrome_check import is_palindrome

def test_standard_palindromes():
    """Test typical palindrome scenarios"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_non_palindromes():
    """Test strings that are not palindromes"""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("race a car") == False

def test_edge_cases():
    """Test edge case scenarios"""
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome(" ") == True  # Blank space
    assert is_palindrome("a") == True  # Single character
    assert is_palindrome("Aa") == True  # Case insensitive
    
def test_special_characters():
    """Test palindromes with special characters"""
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("1A2b22b2A1") == True
    
def test_invalid_inputs():
    """Test various input types"""
    with pytest.raises(TypeError):
        is_palindrome(None)
    with pytest.raises(TypeError):
        is_palindrome(123)