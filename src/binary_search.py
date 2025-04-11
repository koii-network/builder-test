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
        ValueError: If the input list is not sorted
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list is sorted 
    if arr != sorted(arr):
        raise ValueError("Input list must be sorted in ascending order")
    
    # Handle empty list case
    if not arr:
        return -1
    
    # Standard binary search implementation
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # Calculate midpoint to avoid potential integer overflow
        mid = left + (right - left) // 2
        
        # Check if target is found
        if arr[mid] == target:
            return mid
        
        # If target is less than mid, search left half
        elif arr[mid] > target:
            right = mid - 1
        
        # If target is greater than mid, search right half
        else:
            left = mid + 1
    
    # Target not found
    return -1