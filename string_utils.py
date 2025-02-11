def reverse_string(input_str: str) -> str:
    """
    Reverses the given input string.
    
    Args:
        input_str (str): The string to be reversed.
    
    Returns:
        str: The reversed string.
    """
    return input_str[::-1]

# Example usage
if __name__ == "__main__":
    test_string = "Hello, World!"
    print(f"Original string: {test_string}")
    print(f"Reversed string: {reverse_string(test_string)}")