def flatten_array(arr):
    """
    Recursively flatten a nested array into a single-level array.
    
    Args:
        arr (list): A potentially nested list to be flattened.
    
    Returns:
        list: A flattened version of the input array.
    
    Raises:
        TypeError: If the input is not a list or contains non-list/non-iterable items.
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Result list to store flattened elements
    result = []
    
    # Iterate through each element in the input array
    for item in arr:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            result.extend(flatten_array(item))
        # If the item is not a list, add it directly
        else:
            result.append(item)
    
    return result