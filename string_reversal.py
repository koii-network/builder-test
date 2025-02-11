def reverse_string(input_string):
    """
    Reverses the input string.
    
    Args:
        input_string (str): The string to be reversed.
    
    Returns:
        str: The reversed string.
    """
    return input_string[::-1]

# Example usage and basic test
if __name__ == "__main__":
    test_string = "Hello, World!"
    reversed_string = reverse_string(test_string)
    print(f"Original string: {test_string}")
    print(f"Reversed string: {reversed_string}")
    assert reversed_string == "!dlroW ,olleH", "String reversal failed"