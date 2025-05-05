from typing import List, Union

def flatten_array(arr: List[Union[int, List]]) -> List[int]:
    """
    Flatten a nested list of integers to a single-level list.
    
    Args:
        arr (List[Union[int, List]]): A potentially nested list of integers.
    
    Returns:
        List[int]: A flattened list of integers.
    
    Raises:
        TypeError: If the input contains non-integer or non-list elements.
    
    Examples:
        >>> flatten_array([1, [2, 3], 4])
        [1, 2, 3, 4]
        >>> flatten_array([1, [2, [3, 4]], 5])
        [1, 2, 3, 4, 5]
    """
    result = []
    
    def _recursive_flatten(item):
        if isinstance(item, int):
            result.append(item)
        elif isinstance(item, list):
            for sub_item in item:
                _recursive_flatten(sub_item)
        else:
            raise TypeError(f"Invalid element type: {type(item)}. Only integers and lists are allowed.")
    
    _recursive_flatten(arr)
    return result