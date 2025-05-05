def reverse_string(s: str) -> str:
    """
    Reverse the given string manually, preserving all original characters.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Validate input is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Manual string reversal using a list and two-pointer technique
    # Convert string to list to allow manipulation
    chars = list(s)
    
    # Two-pointer approach to swap characters
    left, right = 0, len(chars) - 1
    while left < right:
        # Swap characters
        chars[left], chars[right] = chars[right], chars[left]
        
        # Move pointers
        left += 1
        right -= 1
    
    # Convert back to string and return
    return ''.join(chars)