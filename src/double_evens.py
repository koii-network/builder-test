def double_even_numbers(numbers):
    """
    Takes an array of numbers and returns a new array with even numbers doubled.
    
    Args:
        numbers (list): Input list of numbers
    
    Returns:
        list: A new list where even numbers are multiplied by 2, odd numbers remain unchanged
    
    Raises:
        TypeError: If input is not a list or contains non-numeric elements
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check all elements are numeric
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements must be numeric")
    
    # Return new list with even numbers doubled
    return [x * 2 if x % 2 == 0 else x for x in numbers]