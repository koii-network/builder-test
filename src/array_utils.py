from typing import List, Union, Any

def flatten_array(arr: Union[List[Any], Any]) -> List[Any]:
    """
    Recursively flatten a nested array of arbitrary depth into a single-level list.
    
    Args:
        arr (Union[List[Any], Any]): The input array to be flattened. 
                                     Can be a nested list or a single element.
    
    Returns:
        List[Any]: A flattened list containing all elements from the input.
    
    Examples:
        >>> flatten_array([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_array([])
        []
        >>> flatten_array(1)
        [1]
    """
    # Base case: if input is not a list, return it as a single-element list
    if not isinstance(arr, list):
        return [arr]
    
    # If list is empty, return empty list
    if not arr:
        return []
    
    # Recursive flattening
    flattened = []
    for item in arr:
        # Recursively flatten each item and extend the result
        flattened.extend(flatten_array(item))
    
    return flattened