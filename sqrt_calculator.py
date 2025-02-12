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
    
    # Using Newton's method for square root calculation
    if number == 0:
        return 0
    
    # Initial guess
    x = number
    # Iteration to improve accuracy
    while True:
        # Newton's method formula
        root = 0.5 * (x + number / x)
        
        # Check if we've converged to a stable solution
        if abs(root - x) < 1e-9:
            return root
        
        x = root

# Example usage
if __name__ == "__main__":
    try:
        print(f"Square root of 16: {calculate_square_root(16)}")
        print(f"Square root of 2: {calculate_square_root(2)}")
        print(f"Square root of 0: {calculate_square_root(0)}")
        # Uncomment to test error case: print(calculate_square_root(-4))
    except ValueError as e:
        print(f"Error: {e}")