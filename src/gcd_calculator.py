from src.prime_factorization import prime_factorization

def gcd_with_prime_factors(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers using prime factorization.
    
    This function uses prime factorization to compute the GCD efficiently.
    
    Args:
        a (int): First positive integer.
        b (int): Second positive integer.
    
    Returns:
        int: The Greatest Common Divisor of a and b.
    
    Raises:
        TypeError: If inputs are not integers.
        ValueError: If inputs are not positive integers.
    """
    # Input validation
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Inputs must be integers")
    
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # If numbers are the same, return the number
    if a == b:
        return a
    
    # Get prime factorizations
    a_factors = prime_factorization(a)
    b_factors = prime_factorization(b)
    
    # Find the common prime factors
    gcd_factors = []
    a_factor_counts = {}
    b_factor_counts = {}
    
    # Count occurrences of prime factors
    for factor in a_factors:
        a_factor_counts[factor] = a_factor_counts.get(factor, 0) + 1
    
    for factor in b_factors:
        b_factor_counts[factor] = b_factor_counts.get(factor, 0) + 1
    
    # Find common factors with their minimum counts
    for factor, count in a_factor_counts.items():
        if factor in b_factor_counts:
            common_count = min(count, b_factor_counts[factor])
            gcd_factors.extend([factor] * common_count)
    
    # If no common factors, return 1
    if not gcd_factors:
        return 1
    
    # Calculate GCD by multiplying common prime factors
    gcd = 1
    for factor in gcd_factors:
        gcd *= factor
    
    return gcd