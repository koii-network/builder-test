def is_prime(n):
    """
    Check if a given number is prime.
    
    Args:
        n (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # Handle edge cases
    if n <= 1:
        return False
    
    # Check for divisibility from 2 to square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_numbers = [2, 3, 4, 5, 6, 7, 11, 13, 17, 20, 0, 1, 25]
    
    for num in test_numbers:
        print(f"{num} is prime: {is_prime(num)}")