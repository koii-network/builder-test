from typing import List, Union

def flatten_array(arr: List[Union[int, List]]) -> List[int]:
    """
    Flatten a nested list of integers to a single-level list.
    
    This function recursively flattens a potentially nested list of integers,
    handling various levels of nesting and different types of nested structures.
    
    Args:
        arr (List[Union[int, List]]): A potentially nested list of integers
    
    Returns:
        List[int]: A flattened list of integers
    
    Raises:
        TypeError: If the input contains non-integer non-list elements
    
    Examples:
        >>> flatten_array([1, [2, 3], 4])
        [1, 2, 3, 4]
        >>> flatten_array([1, [2, [3, 4]], 5])
        [1, 2, 3, 4, 5]
    """
    # Handle None or empty input
    if arr is None:
        return []
    
    # Result list to store flattened elements
    flattened = []
    
    # Iterate through each element in the input list
    for item in arr:
        # If item is a list, recursively flatten it
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        # If item is an integer, append it directly
        elif isinstance(item, int):
            flattened.append(item)
        # Raise error for unsupported types
        else:
            raise TypeError(f"Unsupported type in array: {type(item)}")
    
    return flattened