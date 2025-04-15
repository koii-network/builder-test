def reverse_string(s: str) -> str:
    """
    Reverses the given string manually without using slicing or built-in reverse methods.

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
    
    # Convert string to list of characters to allow manipulation
    chars = list(s)
    
    # Manually reverse the list of characters
    left, right = 0, len(chars) - 1
    while left < right:
        # Swap characters from both ends
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    # Convert back to string and return
    return ''.join(chars)