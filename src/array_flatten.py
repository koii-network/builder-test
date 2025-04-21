from typing import List, Union

def flatten_array(nested_array: List[Union[int, List]]) -> List[int]:
    """
    Flatten a nested array of integers into a single-level array.
    
    Args:
        nested_array (List[Union[int, List]]): An array that may contain 
                                               integers or nested lists of integers.
    
    Returns:
        List[int]: A flattened list containing all integers from the input.
    
    Raises:
        TypeError: If the input contains non-integer and non-list elements.
    
    Examples:
        >>> flatten_array([1, [2, 3], 4])
        [1, 2, 3, 4]
        >>> flatten_array([1, [2, [3, 4]], 5])
        [1, 2, 3, 4, 5]
    """
    # Validate input type
    if not isinstance(nested_array, list):
        raise TypeError("Input must be a list")
    
    # Recursive flattening function
    def _flatten(item):
        # If item is an integer, return it as a single-element list
        if isinstance(item, int):
            return [item]
        
        # If item is a list, recursively flatten it
        if isinstance(item, list):
            flattened = []
            for sub_item in item:
                flattened.extend(_flatten(sub_item))
            return flattened
        
        # Raise error for unsupported types
        raise TypeError(f"Unsupported type in array: {type(item)}")
    
    # Flatten the entire input array
    return _flatten(nested_array)