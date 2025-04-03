"""
Test suite for input validation module.
"""

import pytest
from src.input_validator import (
    validate_email, 
    validate_age, 
    validate_list_input, 
    ValidationError
)


def test_validate_email_valid():
    """Test valid email addresses."""
    assert validate_email("user@example.com") == "user@example.com"
    assert validate_email("  user@example.com  ") == "user@example.com"


def test_validate_email_invalid():
    """Test invalid email addresses."""
    with pytest.raises(ValidationError, match="Invalid email format"):
        validate_email("invalid-email")
    
    with pytest.raises(ValidationError, match="Email cannot be empty"):
        validate_email("")
    
    with pytest.raises(ValidationError, match="Email must be a string"):
        validate_email(123)


def test_validate_age_valid():
    """Test valid age inputs."""
    assert validate_age(25) == 25
    assert validate_age("30") == 30


def test_validate_age_invalid():
    """Test invalid age inputs."""
    with pytest.raises(ValidationError, match="Age must be a valid integer"):
        validate_age("not a number")
    
    with pytest.raises(ValidationError, match="Age cannot be negative"):
        validate_age(-5)
    
    with pytest.raises(ValidationError, match="Age is unrealistically high"):
        validate_age(200)


def test_validate_list_input():
    """Test list input validation."""
    # Basic list validation
    assert validate_list_input([1, 2, 3]) == [1, 2, 3]
    
    # List with min and max length
    assert validate_list_input([1, 2], min_length=2, max_length=3) == [1, 2]
    
    # List with item validator
    validated = validate_list_input(
        ["user1@example.com", "user2@example.com"], 
        item_validator=validate_email
    )
    assert validated == ["user1@example.com", "user2@example.com"]


def test_validate_list_input_invalid():
    """Test invalid list input scenarios."""
    # Not a list
    with pytest.raises(ValidationError, match="Input must be a list"):
        validate_list_input("not a list")
    
    # Too few items
    with pytest.raises(ValidationError, match="List must have at least 2 items"):
        validate_list_input([1], min_length=2)
    
    # Too many items
    with pytest.raises(ValidationError, match="List cannot have more than 3 items"):
        validate_list_input([1, 2, 3, 4], max_length=3)
    
    # Invalid item in list
    with pytest.raises(ValidationError, match="List item validation failed"):
        validate_list_input(
            ["valid@email.com", "invalid-email"], 
            item_validator=validate_email
        )