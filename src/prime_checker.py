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
    # Check for invalid inputs
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    
    # Handle special cases
    if number <= 1:
        return False
    
    # Handle 2 as a special case (the only even prime number)
    if number == 2:
        return True
    
    # Even numbers greater than 2 are not prime
    if number % 2 == 0:
        return False
    
    # Check odd divisors up to the square root of the number
    for divisor in range(3, int(number**0.5) + 1, 2):
        if number % divisor == 0:
            return False
    
    return True