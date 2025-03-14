import pytest
from src.palindrome import is_palindrome

def test_simple_palindromes():
    """Test basic palindrome scenarios."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("madam") == True
    assert is_palindrome("") == True

def test_palindromes_with_spaces_and_punctuation():
    """Test palindromes with spaces, punctuation, and mixed case."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("Race a car") == False
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_non_palindromes():
    """Test non-palindrome scenarios."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_single_character():
    """Test single character strings."""
    assert is_palindrome("a") == True
    assert is_palindrome("Z") == True

def test_numeric_palindromes():
    """Test numeric palindromes."""
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("123 456") == False

def test_mixed_alphanumeric():
    """Test alphanumeric palindromes."""
    assert is_palindrome("a1b2c33c2b1a") == True
    assert is_palindrome("a1b2c3") == False