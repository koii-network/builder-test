from src.prime_factorization import prime_factorization

def gcd_using_prime_factors(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers using prime factorization.
    
    This function computes the GCD by finding the common prime factors between 
    the two input numbers and multiplying them.
    
    Args:
        a (int): First positive integer.
        b (int): Second positive integer.
    
    Returns:
        int: The Greatest Common Divisor of a and b.
    
    Raises:
        ValueError: If either input is not a positive integer.
    """
    # Validate inputs
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers")
    
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # Special case: if either number is 1, GCD is 1
    if a == 1 or b == 1:
        return 1
    
    # Get prime factorizations of both numbers
    a_factors = prime_factorization(a)
    b_factors = prime_factorization(b)
    
    # Find common prime factors
    gcd_factors = []
    a_factor_count = {}
    b_factor_count = {}
    
    # Count occurrences of prime factors
    for factor in a_factors:
        a_factor_count[factor] = a_factor_count.get(factor, 0) + 1
    
    for factor in b_factors:
        b_factor_count[factor] = b_factor_count.get(factor, 0) + 1
    
    # Determine common prime factors with their minimum occurrence
    for factor in set(a_factor_count.keys()) & set(b_factor_count.keys()):
        common_count = min(a_factor_count[factor], b_factor_count[factor])
        gcd_factors.extend([factor] * common_count)
    
    # Calculate GCD by multiplying common prime factors
    if not gcd_factors:
        return 1  # If no common factors, GCD is 1
    
    gcd = 1
    for factor in gcd_factors:
        gcd *= factor
    
    return gcd