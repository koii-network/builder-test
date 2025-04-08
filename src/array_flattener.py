from typing import List, Union, Any

def flatten_array(arr: List[Union[Any, List]]) -> List[Any]:
    """
    Recursively flattens a nested array into a single-level list.
    
    Args:
        arr (List[Union[Any, List]]): A potentially nested list to be flattened.
    
    Returns:
        List[Any]: A flattened list containing all non-list elements.
    
    Raises:
        TypeError: If the input is not a list.
    
    Examples:
        >>> flatten_array([1, [2, 3], 4])
        [1, 2, 3, 4]
        >>> flatten_array([1, [2, [3, 4]], 5])
        [1, 2, 3, 4, 5]
        >>> flatten_array([])
        []
    """
    # Validate input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Recursive flattening implementation
    flattened = []
    for item in arr:
        # If item is a list, recursively flatten
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        # If item is not a list, add to flattened list
        else:
            flattened.append(item)
    
    return flattened