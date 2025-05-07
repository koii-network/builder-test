from typing import List, Union, Any

def flatten(arr: Union[List[Any], Any]) -> List[Any]:
    """
    Recursively flatten a nested list into a single-level list.
    
    Args:
        arr (Union[List[Any], Any]): Input list that may contain nested lists.
    
    Returns:
        List[Any]: A flattened list with all nested elements extracted.
    
    Raises:
        TypeError: If input is not a list and cannot be flattened.
    """
    # Base case: if input is not a list, return it as a single-element list
    if not isinstance(arr, list):
        return [arr]
    
    # Recursive flattening
    flattened = []
    for item in arr:
        # Recursively flatten each item
        if isinstance(item, list):
            flattened.extend(flatten(item))
        else:
            flattened.append(item)
    
    return flattened