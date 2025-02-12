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
    # Check for negative input
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Handle base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Iterative approach for efficiency
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

# Example usage and basic tests
if __name__ == "__main__":
    # Test some known Fibonacci sequence terms
    test_cases = [
        (0, 0),   # First term
        (1, 1),   # Second term
        (2, 1),   # Third term
        (5, 5),   # Sixth term
        (10, 55)  # 11th term
    ]
    
    for n, expected in test_cases:
        result = fibonacci(n)
        print(f"fibonacci({n}) = {result}")
        assert result == expected, f"Failed for n={n}"
    
    print("All tests passed successfully!")