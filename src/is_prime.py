def is_prime(n):
    """
    Check if a given number is prime.
    
    Args:
        n (int): A positive integer to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    
    Raises:
        ValueError: If the input is less than 2.
        TypeError: If the input is not an integer.
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        raise ValueError("Input must be a positive integer greater than or equal to 2")
    
    # 2 is prime
    if n == 2:
        return True
    
    # Even numbers greater than 2 are not prime
    if n % 2 == 0:
        return False
    
    # Check odd factors up to the square root of n
    for factor in range(3, int(n**0.5) + 1, 2):
        if n % factor == 0:
            return False
    
    return True