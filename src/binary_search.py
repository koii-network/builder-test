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
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list is sorted
    if any(arr[i] > arr[i+1] for i in range(len(arr)-1)):
        raise ValueError("Input list must be sorted in ascending order")
    
    # Empty list check
    if not arr:
        return -1
    
    # Binary search implementation
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Found the target
        if arr[mid] == target:
            return mid
        
        # Target is in the left half
        elif arr[mid] > target:
            right = mid - 1
        
        # Target is in the right half
        else:
            left = mid + 1
    
    # Target not found
    return -1