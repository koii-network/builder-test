def calculate_square_root(number):
    """
    Calculate the square root of a given number using Newton's method.
    
    Args:
        number (float): The number to calculate the square root of.
    
    Returns:
        float: The square root of the input number.
        
    Raises:
        ValueError: If the input number is negative.
    """
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    
    if number == 0:
        return 0
    
    # Initial guess
    guess = number / 2
    
    # Newton's method for approximating square root
    for _ in range(10):  # Limit iterations to prevent infinite loop
        new_guess = 0.5 * (guess + number / guess)
        
        # If the new guess is very close to the previous guess, we've converged
        if abs(new_guess - guess) < 1e-10:
            return new_guess
        
        guess = new_guess
    
    return guess

# Example usage
if __name__ == "__main__":
    test_numbers = [0, 4, 9, 16, 25]
    for num in test_numbers:
        print(f"Square root of {num}: {calculate_square_root(num)}")