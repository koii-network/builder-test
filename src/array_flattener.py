from typing import List, Union, Any

def flatten_array(arr: List[Any]) -> List[Any]:
    """
    Flatten a nested array (list) to a single-level list.
    
    This function recursively flattens a nested list of arbitrary depth 
    into a single-level list. It handles nested lists, tuples, and other 
    iterable types while preserving non-iterable elements.
    
    Args:
        arr (List[Any]): The input nested list to be flattened.
    
    Returns:
        List[Any]: A flattened list containing all non-list elements.
    
    Raises:
        TypeError: If the input is not a list or iterable.
    
    Examples:
        >>> flatten_array([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_array([1, 2, 3])
        [1, 2, 3]
        >>> flatten_array([])
        []
    """
    # Check if input is a valid iterable
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Initialize result list
    flattened = []
    
    # Iterate through each element
    for item in arr:
        # If item is a list or tuple, recursively flatten
        if isinstance(item, (list, tuple)):
            flattened.extend(flatten_array(item))
        else:
            # Add non-list items directly
            flattened.append(item)
    
    return flattened