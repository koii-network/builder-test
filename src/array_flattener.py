from typing import List, Union, Any, Iterable, Tuple

def flatten_array(arr: Union[List[Any], Tuple[Any, ...]]) -> List[Any]:
    """
    Flatten a nested array (list or tuple) to a single-level list.
    
    This function recursively flattens a nested list or tuple of arbitrary depth 
    into a single-level list. It handles nested lists, tuples, and other 
    iterable types while preserving non-iterable elements.
    
    Args:
        arr (Union[List[Any], Tuple[Any, ...]]): The input nested list/tuple to be flattened.
    
    Returns:
        List[Any]: A flattened list containing all non-list/non-tuple elements.
    
    Raises:
        TypeError: If the input is not a list or tuple.
    
    Examples:
        >>> flatten_array([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_array([1, 2, 3])
        [1, 2, 3]
        >>> flatten_array([])
        []
    """
    # Check if input is a valid iterable
    if not isinstance(arr, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    
    # Initialize result list
    flattened = []
    
    # Iterate through each element
    for item in arr:
        # If item is a list or tuple, recursively flatten
        if isinstance(item, (list, tuple)):
            flattened.extend(flatten_array(item))
        else:
            # Add non-list/non-tuple items directly
            flattened.append(item)
    
    return flattened