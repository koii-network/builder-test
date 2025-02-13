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
    
    # Handle zero and positive numbers
    if number == 0:
        return 0
    
    # Use Newton's method for square root approximation
    guess = number / 2  # Initial guess
    
    for _ in range(10):  # Limit iterations to prevent infinite loop
        next_guess = 0.5 * (guess + number / guess)
        
        # If the guess is very close to the previous guess, return it
        if abs(next_guess - guess) < 1e-10:
            return next_guess
        
        guess = next_guess
    
    return guess