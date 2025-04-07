def is_prime(number):
    """
    Check if a given number is prime.
    
    A prime number is a natural number greater than 1 that is only divisible by 1 and itself.
    
    Args:
        number (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    
    Raises:
        ValueError: If the input is not an integer.
        ValueError: If the input is less than or equal to 0.
    """
    # Validate input
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    
    # Numbers less than or equal to 1 are not prime
    if number <= 1:
        return False
    
    # Check for divisibility from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    return True