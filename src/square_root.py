def calculate_square_root(number):
    """
    Calculate the square root of a given number.
    
    Args:
        number (int or float): The number to calculate the square root of.
    
    Returns:
        float: The square root of the number.
    
    Raises:
        ValueError: If the input number is negative.
        TypeError: If the input is not a number.
    """
    # Check if input is a valid number
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number")
    
    # Check for negative numbers
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    
    # Special case for 0
    if number == 0:
        return 0
    
    # Use Newton's method for square root approximation
    # Initial guess is half of the number
    x = number / 2
    
    # Iterate to improve approximation
    for _ in range(10):  # Typically 10 iterations provide good precision
        x = 0.5 * (x + number / x)
    
    return x