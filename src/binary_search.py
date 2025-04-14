def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target element.
    
    Args:
        arr (list): A sorted list of comparable elements
        target: The element to search for
    
    Returns:
        int: Index of the target element if found, otherwise -1
    
    Raises:
        TypeError: If input is not a list
        ValueError: If the list is not sorted
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list is sorted
    if arr != sorted(arr):
        raise ValueError("Input list must be sorted in ascending order")
    
    # Handle empty list
    if not arr:
        return -1
    
    # Perform binary search
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if target is found
        if arr[mid] == target:
            return mid
        
        # Adjust search boundaries
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # Target not found
    return -1