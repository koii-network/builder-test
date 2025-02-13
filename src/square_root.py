def calculate_square_root(number):
    """
    Calculate the square root of a given number.
    
    Args:
        number (float or int): The number to calculate the square root of.
    
    Returns:
        float: The square root of the input number.
    
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
    
    # Special case for zero
    if number == 0:
        return 0
    
    # Newton-Raphson method for square root calculation
    x = number
    y = (x + number / x) / 2
    
    # Iterate until we get a very close approximation
    while abs(y - x) > 0.00001:
        x = y
        y = (x + number / x) / 2
    
    return y