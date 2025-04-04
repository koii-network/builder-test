from typing import Union, List, Dict, Any

class InputValidationError(ValueError):
    """Custom exception for input validation errors."""
    pass

def validate_user_input(
    input_data: Union[str, int, List[Any], Dict[str, Any]], 
    required_type: type = None, 
    min_length: int = None, 
    max_length: int = None, 
    allowed_values: List[Any] = None
) -> Union[str, int, List[Any], Dict[str, Any]]:
    """
    Validate user input with comprehensive checks.
    
    Args:
        input_data: The input to validate
        required_type: Expected type of input
        min_length: Minimum allowed length (for strings, lists, dicts)
        max_length: Maximum allowed length (for strings, lists, dicts)
        allowed_values: List of permitted values
    
    Returns:
        Validated input data
    
    Raises:
        InputValidationError: If input fails validation
    """
    # Check for None input
    if input_data is None:
        raise InputValidationError("Input cannot be None")
    
    # Type validation
    if required_type is not None and not isinstance(input_data, required_type):
        raise InputValidationError(f"Input must be of type {required_type.__name__}, "
                                   f"got {type(input_data).__name__}")
    
    # Length validation (for strings, lists, dicts)
    if min_length is not None:
        if isinstance(input_data, (str, list, dict)) and len(input_data) < min_length:
            raise InputValidationError(f"Input length must be at least {min_length}")
    
    if max_length is not None:
        if isinstance(input_data, (str, list, dict)) and len(input_data) > max_length:
            raise InputValidationError(f"Input length must not exceed {max_length}")
    
    # Allowed values validation
    if allowed_values is not None:
        if input_data not in allowed_values:
            raise InputValidationError(f"Input must be one of {allowed_values}")
    
    return input_data