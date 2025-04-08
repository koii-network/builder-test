def is_prime(number):
    """
    Check if a given number is prime.
    
    A prime number is a natural number greater than 1 that is only divisible by 1 and itself.
    
    Args:
        number (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is less than or equal to 0.
    """
    # Check input type
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Check input range
    if number <= 0:
        raise ValueError("Input must be a positive integer greater than 0")
    
    # Special cases
    if number == 1:
        return False
    
    if number == 2:
        return True
    
    # Optimization: Check if even and greater than 2
    if number % 2 == 0:
        return False
    
    # Check odd divisors up to the square root of the number
    for divisor in range(3, int(number**0.5) + 1, 2):
        if number % divisor == 0:
            return False
    
    return True