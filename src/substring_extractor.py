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
    
    # Use a list to preserve order and a set for uniqueness
    unique_substrings = []
    unique_set = set()
    
    # Generate all possible substrings
    for start in range(len(input_string)):
        for end in range(start + 1, len(input_string) + 1):
            substring = input_string[start:end]
            if substring not in unique_set:
                unique_substrings.append(substring)
                unique_set.add(substring)
    
    return unique_substrings