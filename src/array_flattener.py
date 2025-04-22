from typing import List, Union

def flatten_array(arr: List[Union[int, List]]) -> List[int]:
    """
    Recursively flatten a nested list of integers into a single-level list.
    
    Args:
        arr (List[Union[int, List]]): A potentially nested list of integers.
    
    Returns:
        List[int]: A flattened list containing all integers from the input.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer/non-list elements.
    
    Examples:
        >>> flatten_array([1, [2, 3], 4])
        [1, 2, 3, 4]
        >>> flatten_array([1, [2, [3, 4]], 5])
        [1, 2, 3, 4, 5]
    """
    # Validate input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    flattened = []
    
    for item in arr:
        # If item is a list, recursively flatten
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        # If item is an integer, append to result
        elif isinstance(item, int):
            flattened.append(item)
        # Raise error for invalid item types
        else:
            raise TypeError(f"List can only contain integers or nested lists, found {type(item)}")
    
    return flattened