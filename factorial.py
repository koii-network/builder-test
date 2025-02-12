def factorial(n):
    """
    Calculate the factorial of a non-negative integer.
    
    Args:
        n (int): A non-negative integer
    
    Returns:
        int: The factorial of the input number
    
    Raises:
        ValueError: If the input is negative
    """
    # Check for negative input
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Base cases
    if n == 0 or n == 1:
        return 1
    
    # Recursive calculation
    return n * factorial(n - 1)

# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_cases = [0, 1, 5, 10]
    
    for num in test_cases:
        print(f"Factorial of {num} is: {factorial(num)}")