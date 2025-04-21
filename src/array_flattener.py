from typing import List, Union

def flatten_array(arr: List[Union[int, List]]) -> List[int]:
    """
    Flatten a nested list of integers into a single-level list.
    
    This function recursively flattens a potentially nested list of integers,
    handling various levels of nesting and different types of nested lists.
    
    Args:
        arr (List[Union[int, List]]): A potentially nested list of integers
    
    Returns:
        List[int]: A flattened list of integers
    
    Raises:
        TypeError: If non-integer or non-list elements are found
    
    Examples:
        >>> flatten_array([1, [2, 3], 4])
        [1, 2, 3, 4]
        >>> flatten_array([1, [2, [3, 4]], 5])
        [1, 2, 3, 4, 5]
    """
    flattened = []
    
    for item in arr:
        if isinstance(item, int):
            flattened.append(item)
        elif isinstance(item, list):
            # Recursively flatten nested lists
            flattened.extend(flatten_array(item))
        else:
            # Raise TypeError for invalid input types
            raise TypeError(f"Invalid type in array: {type(item)}. Only integers and lists are allowed.")
    
    return flattened