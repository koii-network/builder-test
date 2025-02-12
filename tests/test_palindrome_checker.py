import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True

def test_palindrome_with_spaces_and_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_case_sensitivity():
    assert is_palindrome("Racecar") == True

def test_empty_and_single_char_strings():
    assert is_palindrome("") == True
    assert is_palindrome("a") == True

def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_error_handling():
    with pytest.raises(TypeError):
        is_palindrome(123)
    with pytest.raises(TypeError):
        is_palindrome(None)

def test_unicode_palindromes():
    assert is_palindrome("मलयालम") == True  # Malayalam palindrome
    assert is_palindrome("あいうえおおえういあ") == True  # Japanese palindrome