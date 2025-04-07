def is_prime(n):
    """
    Check if a given number is prime.
    
    Args:
        n (int): Number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    
    Raises:
        ValueError: If input is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Handle special cases
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    # Optimization: check divisibility up to square root
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check for primality using 6k ± 1 optimization
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True