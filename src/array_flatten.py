from typing import List, Union

def flatten_array(arr: List[Union[int, List]]) -> List[int]:
    """
    Recursively flatten a nested array of integers into a single-level list.
    
    Args:
        arr (List[Union[int, List]]): A potentially nested list of integers
    
    Returns:
        List[int]: A flattened list of integers
    
    Raises:
        TypeError: If the input contains non-integer and non-list elements
    """
    flattened = []
    
    for item in arr:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        # If the item is an integer, add it to the flattened list
        elif isinstance(item, int):
            flattened.append(item)
        # Raise an error for non-integer and non-list elements
        else:
            raise TypeError(f"Invalid element type: {type(item)}. Only integers and lists are allowed.")
    
    return flattened