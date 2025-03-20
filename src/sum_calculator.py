def calculate_sum(my_list):
    """
    Calculate the sum of a list of integers where each number is multiplied by its index.
    
    Args:
        my_list (list): A list of integers to be summed.
    
    Returns:
        int: The sum of each number multiplied by its index.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Check if input is a list
    if not isinstance(my_list, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in my_list):
        raise TypeError("All list elements must be integers")
    
    # Calculate sum using index multiplication
    return sum(num * index for index, num in enumerate(my_list))