def reverse_string(input_str: str) -> str:
    """
    Reverses the input string.
    
    Args:
        input_str (str): The string to be reversed.
    
    Returns:
        str: The reversed string.
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(input_str, str):
        raise TypeError("Input must be a string")
    
    return input_str[::-1]