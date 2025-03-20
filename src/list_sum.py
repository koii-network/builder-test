def calculate_sum(my_list):
    """
    Calculate the sum of list elements, where each element is multiplied by its index.
    
    Args:
        my_list (list): A list of integers to be summed.
    
    Returns:
        int: The sum of each element multiplied by its index.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input is a list
    if not isinstance(my_list, list):
        raise TypeError("Input must be a list")
    
    # Validate list contains only integers
    if not all(isinstance(x, int) for x in my_list):
        raise TypeError("List must contain only integers")
    
    # Calculate sum by multiplying each element by its index
    return sum(num * index for index, num in enumerate(my_list))