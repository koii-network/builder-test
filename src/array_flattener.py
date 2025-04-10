from typing import List, Union

def flatten_array(arr: List[Union[int, List]]) -> List[int]:
    """
    Recursively flatten a nested array of integers.

    This function takes a potentially nested list and returns a 
    flat list containing all integer elements from the original list.

    Args:
        arr (List[Union[int, List]]): A potentially nested list of integers.

    Returns:
        List[int]: A flattened list containing all integer elements.

    Examples:
        >>> flatten_array([1, [2, 3], 4])
        [1, 2, 3, 4]
        >>> flatten_array([1, [2, [3, 4]], 5])
        [1, 2, 3, 4, 5]
        >>> flatten_array([])
        []
    """
    # Handle base cases
    if not arr:
        return []
    
    # Recursive flattening
    flattened = []
    for item in arr:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        # If the item is an integer, add it to the list
        elif isinstance(item, int):
            flattened.append(item)
        # Ignore other types
        else:
            continue
    
    return flattened