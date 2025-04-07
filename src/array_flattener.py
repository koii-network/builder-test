from typing import List, Union

def flatten_array(arr: List[Union[int, List]]) -> List[int]:
    """
    Flatten a nested list of integers into a single-level list.
    
    This function recursively flattens a nested list, handling 
    lists of various depth levels.
    
    Args:
        arr (List[Union[int, List]]): A potentially nested list of integers.
    
    Returns:
        List[int]: A flattened list containing all integers.
    
    Raises:
        TypeError: If the input contains non-integer and non-list elements.
    
    Examples:
        >>> flatten_array([1, [2, 3], 4])
        [1, 2, 3, 4]
        >>> flatten_array([1, [2, [3, 4]], 5])
        [1, 2, 3, 4, 5]
        >>> flatten_array([])
        []
    """
    # Handle empty list case
    if not arr:
        return []
    
    # Initialize flattened result list
    flattened = []
    
    # Iterate through each element in the input array
    for item in arr:
        # If item is a list, recursively flatten it
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        # If item is an integer, append it
        elif isinstance(item, int):
            flattened.append(item)
        # Raise error for unsupported types
        else:
            raise TypeError(f"Invalid element type: {type(item)}. Only integers and lists are allowed.")
    
    return flattened