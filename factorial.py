def factorial(n):
    """
    Calculate the factorial of a non-negative integer.
    
    Args:
        n (int): A non-negative integer.
    
    Returns:
        int: The factorial of the input number.
    
    Raises:
        ValueError: If the input is negative.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result

# Example usage
if __name__ == "__main__":
    try:
        print(f"Factorial of 5: {factorial(5)}")
        print(f"Factorial of 0: {factorial(0)}")
        print(f"Factorial of 10: {factorial(10)}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")