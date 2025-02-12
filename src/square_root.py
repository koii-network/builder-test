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
        TypeError: If the input is not a number.
    """
    # Check if input is a number
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number")
    
    # Check for negative numbers
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    
    # Use math.sqrt for precise calculation
    return math.sqrt(number)