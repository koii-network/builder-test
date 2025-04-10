from typing import List, Union

def flatten_array(arr: List[Union[int, List]]) -> List[int]:
    """
    Recursively flatten a nested list of integers.
    
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
    flattened = []
    
    for item in arr:
        if isinstance(item, int):
            flattened.append(item)
        elif isinstance(item, list):
            # Recursively flatten nested lists
            flattened.extend(flatten_array(item))
        else:
            raise TypeError(f"Invalid input: {item}. Only integers and lists are allowed.")
    
    return flattened