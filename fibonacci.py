def fibonacci(n):
    """
    Calculate the nth term in the Fibonacci sequence.
    
    Args:
        n (int): The position of the term to calculate (0-indexed).
    
    Returns:
        int: The nth term in the Fibonacci sequence.
    
    Raises:
        ValueError: If n is negative.
    """
    # Check for invalid input
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Handle base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Initialize first two terms
    a, b = 0, 1
    
    # Iterate to calculate nth term
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

# Example usage and basic testing
if __name__ == "__main__":
    # Test cases
    test_cases = [0, 1, 2, 5, 10]
    for case in test_cases:
        print(f"Fibonacci({case}) = {fibonacci(case)}")