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
    
    # Use Newton's method for square root approximation
    if number == 0:
        return 0
    
    # Initial guess
    x = number
    # Iterate to improve approximation
    for _ in range(10):  # Usually converges quickly
        x = 0.5 * (x + number / x)
    
    return x

# Example usage
if __name__ == "__main__":
    test_numbers = [0, 4, 9, 16, 25]
    for num in test_numbers:
        print(f"Square root of {num}: {calculate_square_root(num)}")