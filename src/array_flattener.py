def flatten_array(arr):
    """
    Flatten a nested array of arbitrary depth into a single-level array.
    
    Args:
        arr (list): A nested list that may contain sublists.
    
    Returns:
        list: A flattened version of the input list.
    
    Raises:
        TypeError: If the input is not a list or contains non-list/non-numeric elements.
    """
    # Validate input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Result to store flattened array
    flattened = []
    
    # Recursive helper function to flatten the array
    def _recursive_flatten(element):
        # If element is a list, recursively flatten it
        if isinstance(element, list):
            for sub_element in element:
                _recursive_flatten(sub_element)
        # If element is a number (int or float), append to flattened list
        elif isinstance(element, (int, float)):
            flattened.append(element)
        # Raise error for non-numeric, non-list elements
        else:
            raise TypeError(f"Invalid element type: {type(element)}")
    
    # Start the recursive flattening
    _recursive_flatten(arr)
    
    return flattened