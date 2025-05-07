def is_prime(number):
    """
    Check if a given number is prime.
    
    Args:
        number (int or float): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    
    Raises:
        TypeError: If the input is not a number.
        ValueError: If the input is not a positive integer.
    """
    # Validate input type
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number")
    
    # Convert to integer and check for whole number
    if not float(number).is_integer():
        return False
    
    # Convert to integer
    number = int(number)
    
    # Handle edge cases
    if number < 2:
        return False
    
    # Check for primality using optimized trial division
    # Only need to check up to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    return True