def calculate_sum(my_list):
    """
    Calculate the sum of numbers in the list, where each number is multiplied by its index.
    
    Args:
        my_list (list): A list of integers to be processed.
    
    Returns:
        int: The sum of each number multiplied by its index.
    
    Raises:
        TypeError: If the input is not a list.
        TypeError: If any element in the list is not an integer.
    """
    # Validate input is a list
    if not isinstance(my_list, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    if not all(isinstance(num, int) for num in my_list):
        raise TypeError("All elements must be integers")
    
    # Calculate weighted sum by multiplying each number with its index
    return sum(num * index for index, num in enumerate(my_list))