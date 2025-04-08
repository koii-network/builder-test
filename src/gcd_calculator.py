from src.prime_factorization import prime_factorization

def gcd_using_prime_factors(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) using prime factorization method.
    
    This function computes the GCD by finding the common prime factors 
    between two numbers and multiplying them.
    
    Args:
        a (int): First positive integer.
        b (int): Second positive integer.
    
    Returns:
        int: The Greatest Common Divisor of a and b.
    
    Raises:
        ValueError: If either input is not a positive integer.
    """
    # Validate inputs
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # Special case: if either number is 0, return the other number
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Get prime factors of both numbers
    a_factors = prime_factorization(a)
    b_factors = prime_factorization(b)
    
    # Find common prime factors
    gcd = 1
    
    # Use two pointers to track factors of a and b
    i, j = 0, 0
    while i < len(a_factors) and j < len(b_factors):
        if a_factors[i] == b_factors[j]:
            # Common prime factor found
            gcd *= a_factors[i]
            i += 1
            j += 1
        elif a_factors[i] < b_factors[j]:
            i += 1
        else:
            j += 1
    
    return gcd