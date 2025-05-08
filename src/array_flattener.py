from typing import List, Union

def flatten_array(arr: List[Union[int, List]]) -> List[int]:
    """
    Recursively flatten a nested array of integers.
    
    Args:
        arr (List[Union[int, List]]): A potentially nested list of integers.
    
    Returns:
        List[int]: A flattened list containing all integers from the input.
    
    Raises:
        TypeError: If the input contains non-integer and non-list elements.
    
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
        # If the item is an integer, add it to the result
        elif isinstance(item, int):
            flattened.append(item)
        # Raise an error for any other type
        else:
            raise TypeError(f"Unsupported type in array: {type(item)}")
    
    return flattened