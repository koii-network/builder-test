def calculate_sum(my_list):
    """
    Calculate the sum of integers in a list, multiplying each number by its index.
    
    Args:
        my_list (list): A list of integers to be summed.
    
    Returns:
        int: The sum of each number multiplied by its index.
    
    Raises:
        TypeError: If the input is not a list.
        TypeError: If the list contains non-integer elements.
    """
    # Validate input is a list
    if not isinstance(my_list, list):
        raise TypeError("Input must be a list")
    
    # Validate list contains only integers
    if not all(isinstance(x, int) for x in my_list):
        raise TypeError("List must contain only integers")
    
    # Calculate sum with index multiplication
    return sum(num * index for index, num in enumerate(my_list))