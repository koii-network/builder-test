def calculate_factorial(n):
    """
    Calculate the factorial of a non-negative integer.
    
    Args:
        n (int): A non-negative integer to calculate factorial for.
    
    Returns:
        int: The factorial of the input number.
    
    Raises:
        ValueError: If the input is negative.
        TypeError: If the input is not an integer.
    """
    # Validate input type
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Validate input range
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Base cases
    if n == 0 or n == 1:
        return 1
    
    # Recursive calculation of factorial
    return n * calculate_factorial(n - 1)