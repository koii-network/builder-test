def is_prime(number):
    """
    Check if a given number is prime.
    
    Args:
        number (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Check for valid input
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    
    # Handle special cases
    if number <= 1:
        return False
    
    # Check for primality by testing divisibility
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    return True