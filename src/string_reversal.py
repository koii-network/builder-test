def reverse_string(s: str) -> str:
    """
    Reverse the given string using a manual character-by-character approach.

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
    
    # Handle empty string case
    if len(s) <= 1:
        return s
    
    # Manual string reversal
    # Convert string to list of characters for easy manipulation
    chars = list(s)
    
    # Two-pointer approach to swap characters
    left, right = 0, len(chars) - 1
    while left < right:
        # Swap characters
        chars[left], chars[right] = chars[right], chars[left]
        
        # Move pointers
        left += 1
        right -= 1
    
    # Convert list back to string and return
    return ''.join(chars)