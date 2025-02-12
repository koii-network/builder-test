def factorial(n):
    """
    Calculate the factorial of a given non-negative integer.
    
    Args:
        n (int): A non-negative integer to calculate factorial for.
    
    Returns:
        int: The factorial of the input number.
    
    Raises:
        ValueError: If input is negative.
    """
    # Check for negative input
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Base cases
    if n == 0 or n == 1:
        return 1
    
    # Recursive calculation
    return n * factorial(n - 1)

# Example usage
if __name__ == "__main__":
    # Test cases
    print(f"Factorial of 0: {factorial(0)}")
    print(f"Factorial of 5: {factorial(5)}")
    print(f"Factorial of 10: {factorial(10)}")