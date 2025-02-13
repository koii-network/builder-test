def fibonacci(n):
    """
    Calculate the nth term in the Fibonacci sequence.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-based index).
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Iterative calculation for better performance
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b