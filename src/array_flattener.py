from typing import List, Union, Any

def flatten_array(nested_list: List[Any]) -> List[Any]:
    """
    Recursively flatten a nested list of arbitrary depth.

    Args:
        nested_list (List[Any]): A potentially nested list to be flattened.

    Returns:
        List[Any]: A flattened list with all nested elements extracted.

    Examples:
        >>> flatten_array([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_array([])
        []
        >>> flatten_array([1, 2, 3])
        [1, 2, 3]
    """
    flattened = []
    
    for item in nested_list:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        else:
            # If not a list, add the item directly
            flattened.append(item)
    
    return flattened