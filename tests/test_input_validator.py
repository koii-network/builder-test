"""
Test suite for input validation module
"""

import pytest
import re
from src.input_validator import validate_input, sanitize_input


def test_validate_input_required():
    # Test required input
    with pytest.raises(ValueError, match="Input is required"):
        validate_input(None, required=True)
    
    # Test empty string for required input
    with pytest.raises(ValueError, match="Input is required"):
        validate_input('', required=True)


def test_validate_input_type():
    # Type validation tests
    assert validate_input(42, type_=int) == 42
    assert validate_input("hello", type_=str) == "hello"
    
    # Type mismatch
    with pytest.raises(TypeError):
        validate_input(42, type_=str)


def test_validate_input_length():
    # Length validation for strings
    assert validate_input("hello", min_length=3, max_length=5) == "hello"
    
    # Too short
    with pytest.raises(ValueError, match="at least 3"):
        validate_input("hi", min_length=3)
    
    # Too long
    with pytest.raises(ValueError, match="at most 5"):
        validate_input("helloworld", max_length=5)


def test_validate_input_regex():
    # Regex validation
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Valid email
    assert validate_input("test@example.com", regex=email_regex) == "test@example.com"
    
    # Invalid email
    with pytest.raises(ValueError, match="does not match"):
        validate_input("invalid-email", regex=email_regex)


def test_validate_input_custom_validator():
    # Custom validator function
    def positive_number(x):
        if x <= 0:
            raise ValueError("Must be a positive number")
    
    # Valid input
    assert validate_input(5, custom_validator=positive_number) == 5
    
    # Invalid input
    with pytest.raises(ValueError, match="Must be a positive number"):
        validate_input(-1, custom_validator=positive_number)


def test_sanitize_input():
    # Whitespace stripping
    assert sanitize_input("  hello world  ") == "hello world"
    
    # Removing special characters
    assert sanitize_input("Hello, World! 123", remove_special_chars=True) == "Hello World 123"
    
    # Non-string inputs
    assert sanitize_input(None) is None
    assert sanitize_input(42) == 42


def test_none_input():
    # None input when not required
    assert validate_input(None) is None
    assert validate_input(None, type_=str) is None