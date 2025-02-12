def reverse_string(input_str):
    """
    Reverse the given string.
    
    Args:
        input_str (str): The string to be reversed.
    
    Returns:
        str: The reversed string.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_str, str):
        raise TypeError("Input must be a string")
    
    # Return the reversed string
    return input_str[::-1]