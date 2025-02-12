def reverse_string(s):
    """
    Reverses the input string.
    
    Args:
        s (str): The input string to be reversed.
    
    Returns:
        str: The reversed string.
    """
    return s[::-1]

# Simple test to demonstrate the function
if __name__ == "__main__":
    test_string = "Hello, World!"
    reversed_string = reverse_string(test_string)
    print(f"Original string: {test_string}")
    print(f"Reversed string: {reversed_string}")