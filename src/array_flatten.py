from typing import List, Union

def flatten_array(arr: List[Union[int, List]]) -> List[int]:
    """
    Flatten a nested list of integers into a single-level list.
    
    This function recursively flattens a list that may contain nested lists 
    of integers into a single-level list of integers.
    
    Args:
        arr (List[Union[int, List]]): A list that may contain integers or nested lists
    
    Returns:
        List[int]: A flattened list of integers
    
    Raises:
        TypeError: If the input contains non-integer and non-list elements
    
    Examples:
        >>> flatten_array([1, [2, 3], 4])
        [1, 2, 3, 4]
        >>> flatten_array([1, [2, [3, 4]], 5])
        [1, 2, 3, 4, 5]
    """
    flattened = []
    
    for item in arr:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        # If the item is an integer, add it to the flattened list
        elif isinstance(item, int):
            flattened.append(item)
        else:
            # Raise an error for non-integer and non-list elements
            raise TypeError(f"Unsupported type in array: {type(item)}")
    
    return flattened