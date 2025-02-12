def reverse_string(s: str) -> str:
    """
    Reverses the input string.
    
    Args:
        s (str): The input string to be reversed.
    
    Returns:
        str: The reversed string.
    
    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("")
        ''
        >>> reverse_string("python")
        'nohtyp'
    """
    return s[::-1]