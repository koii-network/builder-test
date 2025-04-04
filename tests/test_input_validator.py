"""
Test suite for input validation module.

This module contains comprehensive tests for input validation functions,
covering various scenarios and edge cases.
"""

import pytest
from src.input_validator import (
    validate_not_empty, 
    validate_type, 
    validate_email, 
    validate_numeric_range, 
    ValidationError
)


def test_validate_not_empty_success():
    """Test validate_not_empty with valid inputs."""
    assert validate_not_empty("hello") == "hello"
    assert validate_not_empty([1, 2, 3]) == [1, 2, 3]
    assert validate_not_empty({"key": "value"}) == {"key": "value"}


def test_validate_not_empty_failure():
    """Test validate_not_empty with empty or None inputs."""
    with pytest.raises(ValidationError, match="cannot be None"):
        validate_not_empty(None)
    
    with pytest.raises(ValidationError, match="cannot be empty"):
        validate_not_empty("")
    
    with pytest.raises(ValidationError, match="cannot be empty"):
        validate_not_empty([])
    
    with pytest.raises(ValidationError, match="cannot be empty"):
        validate_not_empty({})


def test_validate_type_success():
    """Test validate_type with valid type inputs."""
    assert validate_type(5, int) == 5
    assert validate_type("hello", str) == "hello"
    assert validate_type([1, 2], list) == [1, 2]


def test_validate_type_failure():
    """Test validate_type with incorrect type inputs."""
    with pytest.raises(ValidationError, match="must be of type str"):
        validate_type(5, str)
    
    with pytest.raises(ValidationError, match="must be of type list"):
        validate_type("hello", list)


def test_validate_email_success():
    """Test validate_email with valid email addresses."""
    valid_emails = [
        "user@example.com", 
        "user.name@example.co.uk", 
        "user+tag@example.org"
    ]
    
    for email in valid_emails:
        assert validate_email(email) == email


def test_validate_email_failure():
    """Test validate_email with invalid email addresses."""
    invalid_emails = [
        "", 
        None, 
        "invalid-email", 
        "user@.com", 
        "@example.com", 
        "user@example"
    ]
    
    for email in invalid_emails:
        with pytest.raises(ValidationError):
            validate_email(email)


def test_validate_numeric_range_success():
    """Test validate_numeric_range with valid numeric inputs."""
    assert validate_numeric_range(5, 0, 10) == 5
    assert validate_numeric_range(0, 0, 10) == 0
    assert validate_numeric_range(10, 0, 10) == 10
    assert validate_numeric_range(5.5, 0, 10) == 5.5
    
    # Test when min or max is not specified
    assert validate_numeric_range(5) == 5
    assert validate_numeric_range(5, min_val=0) == 5
    assert validate_numeric_range(5, max_val=10) == 5


def test_validate_numeric_range_failure():
    """Test validate_numeric_range with invalid numeric inputs."""
    with pytest.raises(ValidationError, match="must be greater than or equal to 0"):
        validate_numeric_range(-1, 0, 10)
    
    with pytest.raises(ValidationError, match="must be less than or equal to 10"):
        validate_numeric_range(11, 0, 10)
    
    with pytest.raises(ValidationError, match="must be of type int or float"):
        validate_numeric_range("5", 0, 10)