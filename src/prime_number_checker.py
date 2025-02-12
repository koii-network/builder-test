def is_prime(number):
    """
    Check if a given number is prime.
    
    Args:
        number (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is less than or equal to 1.
    """
    # Check input type
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Check input range
    if number <= 1:
        raise ValueError("Input must be greater than 1")
    
    # Check for primality
    if number == 2:
        return True
    
    # No need to check beyond square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    return True