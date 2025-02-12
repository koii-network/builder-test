def is_prime(n):
    """
    Check if a given number is prime.
    
    Args:
        n (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # Handle edge cases
    if n < 2:
        return False
    
    # Check for divisibility from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

# Test cases
def test_is_prime():
    # Test known prime numbers
    assert is_prime(2) == True, "2 should be prime"
    assert is_prime(3) == True, "3 should be prime"
    assert is_prime(17) == True, "17 should be prime"
    assert is_prime(29) == True, "29 should be prime"
    
    # Test known non-prime numbers
    assert is_prime(1) == False, "1 should not be prime"
    assert is_prime(0) == False, "0 should not be prime"
    assert is_prime(4) == False, "4 should not be prime"
    assert is_prime(15) == False, "15 should not be prime"
    assert is_prime(25) == False, "25 should not be prime"
    
    print("All prime number tests passed!")

# Run tests
if __name__ == "__main__":
    test_is_prime()