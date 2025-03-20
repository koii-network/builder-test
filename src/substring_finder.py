def find_unique_substrings(input_string):
    """
    Find all unique substrings within the given input string.
    
    Args:
        input_string (str): The input string to find substrings from.
    
    Returns:
        list: A list of unique substrings, sorted alphabetically.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check input type
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
    
    # Convert to sorted list for consistent output
    return sorted(list(unique_substrings))