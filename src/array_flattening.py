from typing import List, Union, Any

def flatten_array(arr: List[Union[Any, List]]) -> List[Any]:
    """
    Recursively flatten a nested list into a single-level list.
    
    Args:
        arr (List[Union[Any, List]]): A potentially nested list to be flattened.
    
    Returns:
        List[Any]: A flattened list with all nested elements extracted.
    
    Raises:
        TypeError: If the input is not a list.
    
    Examples:
        >>> flatten_array([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_array([1, 2, 3])
        [1, 2, 3]
        >>> flatten_array([])
        []
    """
    # Validate input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Recursive flattening function
    flattened = []
    for item in arr:
        # If the item is a list, recursively flatten
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        else:
            # Otherwise, append the item directly
            flattened.append(item)
    
    return flattened