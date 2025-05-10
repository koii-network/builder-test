def flatten_array(arr):
    """
    Flatten a nested array (list) of arbitrary depth into a single-level list.
    
    Args:
        arr (list): The input nested list to be flattened.
    
    Returns:
        list: A flattened version of the input list.
    
    Raises:
        TypeError: If the input is not a list or contains non-list/non-numeric elements.
    
    Examples:
        >>> flatten_array([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_array([])
        []
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Recursive flattening implementation
    flattened = []
    for item in arr:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        # If the item is not a list, add it directly
        else:
            flattened.append(item)
    
    return flattened