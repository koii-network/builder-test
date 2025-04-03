"""
Input validation module with comprehensive error handling.

This module provides utility functions for validating and sanitizing input
with clear error messaging and type checking.
"""

def validate_input(value, expected_type, min_length=None, max_length=None, 
                   regex_pattern=None, allow_empty=False):
    """
    Validate input based on multiple criteria with comprehensive error handling.

    Args:
        value: Input value to validate
        expected_type (type): Expected type of input
        min_length (int, optional): Minimum length for strings/lists
        max_length (int, optional): Maximum length for strings/lists
        regex_pattern (str, optional): Regex pattern for string validation
        allow_empty (bool, optional): Whether empty values are allowed

    Raises:
        TypeError: If input does not match expected type
        ValueError: If input fails length or regex validation
    
    Returns:
        The validated input value
    """
    # Check for None value
    if value is None:
        if allow_empty:
            return value
        raise ValueError("Input cannot be None")

    # Type checking
    if not isinstance(value, expected_type):
        raise TypeError(f"Expected {expected_type.__name__}, got {type(value).__name__}")

    # Length validation for strings and lists/collections
    if hasattr(value, '__len__'):
        if min_length is not None and len(value) < min_length:
            raise ValueError(f"Input must be at least {min_length} characters/items long")
        if max_length is not None and len(value) > max_length:
            raise ValueError(f"Input must be no more than {max_length} characters/items long")

    # Empty value check
    if not allow_empty and (value == '' or value == []):
        raise ValueError("Input cannot be empty")

    # Optional regex validation for strings
    if regex_pattern and isinstance(value, str):
        import re
        if not re.match(regex_pattern, value):
            raise ValueError(f"Input does not match required pattern: {regex_pattern}")

    return value