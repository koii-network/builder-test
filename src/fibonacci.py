def fibonacci_nth_term(n):
    """
    Calculate the nth term in the Fibonacci sequence.
    
    Args:
        n (int): The position of the term to calculate (0-indexed).
    
    Returns:
        int: The nth term in the Fibonacci sequence.
    
    Raises:
        ValueError: If n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Iterative approach for efficiency
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b