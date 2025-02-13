def is_prime(number):
    """
    Check if a given number is prime.
    
    Args:
        number (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is less than 2.
    """
    # Check input type
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Check input range
    if number < 2:
        raise ValueError("Input must be 2 or greater")
    
    # Check for primality
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    return True