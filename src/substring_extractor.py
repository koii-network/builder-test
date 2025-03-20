def extract_unique_substrings(input_string):
    """
    Extract all unique substrings from the given input string.
    
    Args:
        input_string (str): The input string to extract substrings from.
    
    Returns:
        list: A list of unique substrings.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty list
    if not input_string:
        return []
    
    # Use a set to store unique substrings
    unique_substrings = set()
    
    # Generate all possible substrings
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string) + 1):
            unique_substrings.add(input_string[i:j])
    
    # Convert set to sorted list for consistent output
    return sorted(list(unique_substrings))