def reverse_string(s: str) -> str:
    """
    Reverse the given string manually, preserving all characters.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Type checking
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Manual string reversal using a list-based approach
    # This preserves all characters including spaces and special characters
    reversed_chars = []
    for i in range(len(s) - 1, -1, -1):
        reversed_chars.append(s[i])
    
    return ''.join(reversed_chars)