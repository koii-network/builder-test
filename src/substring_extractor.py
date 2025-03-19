def extract_unique_substrings(input_string):
    """
    Extract all unique substrings from the given input string.
    
    Args:
        input_string (str): The input string to extract substrings from.
    
    Returns:
        list: A list of unique substrings in the order they are discovered.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Input validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty list
    if not input_string:
        return []
    
    # Use a set to track unique substrings to ensure uniqueness
    unique_substrings = set()
    
    # Generate all possible substrings
    for start in range(len(input_string)):
        for end in range(start + 1, len(input_string) + 1):
            substring = input_string[start:end]
            unique_substrings.add(substring)
    
    # Convert to list to maintain order of discovery
    return list(dict.fromkeys(unique_substrings))