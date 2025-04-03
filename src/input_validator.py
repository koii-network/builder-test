"""
Input Validation and Error Handling Module

This module provides utility functions for input validation 
with comprehensive error handling.
"""

def validate_input(value, type_=None, min_length=None, max_length=None, 
                   regex=None, required=False, custom_validator=None):
    """
    Validate input with multiple configurable checks.
    
    Args:
        value: Input value to validate
        type_: Expected type of the input (optional)
        min_length: Minimum length for string/list inputs (optional)
        max_length: Maximum length for string/list inputs (optional)
        regex: Regular expression pattern to match (optional)
        required: Whether the input is required (default: False)
        custom_validator: Optional custom validation function
    
    Returns:
        Validated input value
    
    Raises:
        ValueError: For various validation failures
        TypeError: For type mismatch errors
    """
    # Check if input is required
    if required and (value is None or value == ''):
        raise ValueError("Input is required and cannot be empty")
    
    # Skip further checks if value is None and not required
    if value is None:
        return value
    
    # Type validation
    if type_ is not None:
        if not isinstance(value, type_):
            raise TypeError(f"Expected type {type_.__name__}, got {type(value).__name__}")
    
    # Length validation (for strings and lists)
    if isinstance(value, (str, list)):
        if min_length is not None and len(value) < min_length:
            raise ValueError(f"Input must have at least {min_length} characters/items")
        
        if max_length is not None and len(value) > max_length:
            raise ValueError(f"Input must have at most {max_length} characters/items")
    
    # Regex validation
    if regex is not None:
        import re
        if not re.match(regex, str(value)):
            raise ValueError(f"Input does not match required pattern: {regex}")
    
    # Custom validator
    if custom_validator is not None:
        try:
            custom_validator(value)
        except Exception as e:
            raise ValueError(f"Custom validation failed: {str(e)}")
    
    return value


def sanitize_input(value, strip_whitespace=True, remove_special_chars=False):
    """
    Sanitize input by optionally stripping whitespace and removing special characters.
    
    Args:
        value: Input value to sanitize
        strip_whitespace: Remove leading/trailing whitespace (default: True)
        remove_special_chars: Remove special characters (default: False)
    
    Returns:
        Sanitized input value
    """
    # Handle None or non-string inputs
    if value is None or not isinstance(value, str):
        return value
    
    # Strip whitespace
    if strip_whitespace:
        value = value.strip()
    
    # Remove special characters
    if remove_special_chars:
        import re
        value = re.sub(r'[^a-zA-Z0-9\s]', '', value)
    
    return value