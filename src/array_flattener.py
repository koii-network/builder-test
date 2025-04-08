from typing import List, Union, Any

def flatten_array(arr: List[Union[Any, List]]) -> List[Any]:
    """
    Recursively flatten a nested array into a single-level array.
    
    Args:
        arr (List[Union[Any, List]]): Input array that may contain nested arrays
    
    Returns:
        List[Any]: A flattened array with all nested elements extracted
    
    Raises:
        TypeError: If input is not a list
    """
    # Validate input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Flattening result list
    flattened = []
    
    # Iterate through each element 
    for item in arr:
        # If item is a list, recursively flatten
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        else:
            # If not a list, add directly to result
            flattened.append(item)
    
    return flattened