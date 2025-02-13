import math

def calculate_square_root(number):
    """
    Calculate the square root of a given number.
    
    Args:
        number (float): The number to calculate the square root of.
    
    Returns:
        float: The square root of the input number.
    
    Raises:
        ValueError: If the input number is negative.
    """
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    
    return math.sqrt(number)