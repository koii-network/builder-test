def calculate_factorial(n):
    """
    Calculate the factorial of a given non-negative integer.
    
    Args:
        n (int): The number to calculate factorial for.
    
    Returns:
        int: The factorial of the input number.
    
    Raises:
        TypeError: If input is not an integer.
        ValueError: If input is a negative integer.
    """
    # Check if input is an integer
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Check if input is non-negative
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Base cases
    if n == 0 or n == 1:
        return 1
    
    # Recursive calculation
    return n * calculate_factorial(n - 1)