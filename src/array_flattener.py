from typing import List, Union

def flatten_array(arr: List[Union[int, List]]) -> List[int]:
    """
    Flatten a nested array of integers to a single-level array.
    
    This function recursively flattens a nested array, handling 
    multiple levels of nesting and preserving the order of elements.
    
    Args:
        arr (List[Union[int, List]]): A potentially nested list of integers
    
    Returns:
        List[int]: A flattened list of integers
    
    Raises:
        TypeError: If input is not a list or contains non-integer/list elements
    
    Examples:
        >>> flatten_array([1, [2, 3], 4])
        [1, 2, 3, 4]
        >>> flatten_array([1, [2, [3, 4]], 5])
        [1, 2, 3, 4, 5]
    """
    # Validate input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Flattening function using recursion
    flattened = []
    for item in arr:
        # If item is a list, recursively flatten
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        # If item is an integer, append to result
        elif isinstance(item, int):
            flattened.append(item)
        # Raise error for invalid types
        else:
            raise TypeError(f"Invalid element type: {type(item)}. Only integers and lists are allowed.")
    
    return flattened