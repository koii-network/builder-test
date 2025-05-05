def reverse_string(s: str) -> str:
    """
    Reverse the given string manually without using slice notation or reverse().

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Convert string to list of characters for manipulation
    chars = list(s)
    
    # Swap characters from start to end
    left, right = 0, len(chars) - 1
    while left < right:
        # Swap characters
        chars[left], chars[right] = chars[right], chars[left]
        
        # Move towards center
        left += 1
        right -= 1
    
    # Convert back to string and return
    return ''.join(chars)