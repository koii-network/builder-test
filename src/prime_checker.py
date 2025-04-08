def is_prime(n):
    """
    Check if a given number is prime.
    
    A prime number is a natural number greater than 1 that is only divisible by 1 and itself.
    
    Args:
        n (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Check for valid input
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    # Handle edge cases
    if n <= 1:
        return False
    
    # Check for divisibility up to the square root of n
    # This is an optimization to reduce unnecessary iterations
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True