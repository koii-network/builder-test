"""
Input Validation Module

This module provides utility functions for input validation 
with comprehensive error handling.
"""

import re
from typing import Any, Union, List, Dict, Optional


class ValidationError(ValueError):
    """Custom exception for input validation errors."""
    pass


def validate_not_empty(value: Any, name: str = 'Input') -> str:
    """
    Validate that a value is not empty.
    
    Args:
        value (Any): The value to validate
        name (str, optional): Name of the input for error message. Defaults to 'Input'.
    
    Returns:
        str: The non-empty input value
    
    Raises:
        ValidationError: If the input is empty or None
    """
    if value is None:
        raise ValidationError(f"{name} cannot be None")
    
    # Handle different types of emptiness
    if isinstance(value, (str, list, dict, set)) and len(value) == 0:
        raise ValidationError(f"{name} cannot be empty")
    
    return value


def validate_type(value: Any, expected_type: type, name: str = 'Input') -> Any:
    """
    Validate the type of an input.
    
    Args:
        value (Any): The value to validate
        expected_type (type): The expected type of the input
        name (str, optional): Name of the input for error message. Defaults to 'Input'.
    
    Returns:
        Any: The validated input value
    
    Raises:
        ValidationError: If the input is not of the expected type
    """
    if not isinstance(value, expected_type):
        raise ValidationError(f"{name} must be of type {expected_type.__name__}")
    
    return value


def validate_email(email: str) -> str:
    """
    Validate email format.
    
    Args:
        email (str): Email address to validate
    
    Returns:
        str: The validated email address
    
    Raises:
        ValidationError: If the email is not in a valid format
    """
    validate_not_empty(email, 'Email')
    validate_type(email, str, 'Email')
    
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        raise ValidationError("Invalid email format")
    
    return email


def validate_numeric_range(
    value: Union[int, float], 
    min_val: Optional[Union[int, float]] = None, 
    max_val: Optional[Union[int, float]] = None, 
    name: str = 'Input'
) -> Union[int, float]:
    """
    Validate that a numeric value is within a specified range.
    
    Args:
        value (Union[int, float]): The numeric value to validate
        min_val (Optional[Union[int, float]], optional): Minimum allowed value
        max_val (Optional[Union[int, float]], optional): Maximum allowed value
        name (str, optional): Name of the input for error message. Defaults to 'Input'.
    
    Returns:
        Union[int, float]: The validated numeric value
    
    Raises:
        ValidationError: If the value is outside the specified range
    """
    validate_type(value, (int, float), name)
    
    if min_val is not None and value < min_val:
        raise ValidationError(f"{name} must be greater than or equal to {min_val}")
    
    if max_val is not None and value > max_val:
        raise ValidationError(f"{name} must be less than or equal to {max_val}")
    
    return value