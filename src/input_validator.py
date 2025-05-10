"""
Input Validation and Error Handling Module

This module provides utility functions for comprehensive input validation 
and error handling with descriptive error messages.
"""

import re
from typing import Union, List, Any


class ValidationError(ValueError):
    """Custom exception for input validation errors."""
    pass


def validate_email(email: str) -> str:
    """
    Validate an email address with comprehensive checks.
    
    Args:
        email (str): Email address to validate
    
    Returns:
        str: Validated email address
    
    Raises:
        ValidationError: If email is invalid
    """
    if not isinstance(email, str):
        raise ValidationError("Email must be a string")
    
    # Trim whitespace
    email = email.strip()
    
    # Check if email is empty
    if not email:
        raise ValidationError("Email cannot be empty")
    
    # Basic email regex pattern
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(email_pattern, email):
        raise ValidationError(f"Invalid email format: {email}")
    
    return email


def validate_age(age: Union[int, str]) -> int:
    """
    Validate age with comprehensive checks.
    
    Args:
        age (int or str): Age to validate
    
    Returns:
        int: Validated age
    
    Raises:
        ValidationError: If age is invalid
    """
    # Convert to int if string
    try:
        age = int(age)
    except (ValueError, TypeError):
        raise ValidationError("Age must be a valid integer")
    
    # Check age range
    if age < 0:
        raise ValidationError("Age cannot be negative")
    
    if age > 150:
        raise ValidationError("Age is unrealistically high")
    
    return age


def validate_list_input(
    input_list: List[Any], 
    min_length: int = 0, 
    max_length: int = float('inf'), 
    item_validator: callable = None
) -> List[Any]:
    """
    Validate a list with optional length and item validation.
    
    Args:
        input_list (list): List to validate
        min_length (int, optional): Minimum allowed list length
        max_length (int, optional): Maximum allowed list length
        item_validator (callable, optional): Function to validate each item
    
    Returns:
        list: Validated list
    
    Raises:
        ValidationError: If list is invalid
    """
    # Check if input is a list
    if not isinstance(input_list, list):
        raise ValidationError("Input must be a list")
    
    # Check list length
    if len(input_list) < min_length:
        raise ValidationError(f"List must have at least {min_length} items")
    
    if len(input_list) > max_length:
        raise ValidationError(f"List cannot have more than {max_length} items")
    
    # Validate individual items if a validator is provided
    if item_validator:
        validated_list = []
        for item in input_list:
            try:
                validated_item = item_validator(item)
                validated_list.append(validated_item)
            except ValidationError as e:
                raise ValidationError(f"List item validation failed: {e}")
        return validated_list
    
    return input_list