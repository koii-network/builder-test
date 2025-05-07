from typing import List, Union, Any

def flatten_list(nested_list: List[Any]) -> List[Any]:
    """
    Recursively flatten a nested list of arbitrary depth into a single-level list.
    
    Args:
        nested_list (List[Any]): A potentially nested list to be flattened.
    
    Returns:
        List[Any]: A flattened list containing all non-list elements.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Validate input is a list
    if not isinstance(nested_list, list):
        raise TypeError("Input must be a list")
    
    # Initialize the flattened list
    flattened = []
    
    # Iterate through each element in the input list
    for item in nested_list:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        # If the item is not a list, add it directly
        else:
            flattened.append(item)
    
    return flattened