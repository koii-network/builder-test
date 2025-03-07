def find_unique_substrings(input_string):
    """
    Find all unique substrings within the given input string.
    
    Args:
        input_string (str): The input string to find substrings from.
    
    Returns:
        list: A list of unique substrings from the input string.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Validate input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return an empty list
    if not input_string:
        return []
    
    # Use a set to store unique substrings
    unique_substrings = set()
    
    # Generate all possible substrings
    for start in range(len(input_string)):
        for end in range(start + 1, len(input_string) + 1):
            unique_substrings.add(input_string[start:end])
    
    # Convert set to sorted list for consistent output
    return sorted(list(unique_substrings))