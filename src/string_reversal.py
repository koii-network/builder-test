def reverse_string(s: str) -> str:
    """
    Reverses the given string using a manual character-by-character approach.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Validate input
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Convert string to list of characters for manipulation
    chars = list(s)
    
    # Manual reversal using two-pointer technique
    left, right = 0, len(chars) - 1
    while left < right:
        # Swap characters
        chars[left], chars[right] = chars[right], chars[left]
        
        # Move pointers
        left += 1
        right -= 1
    
    # Convert back to string and return
    return ''.join(chars)