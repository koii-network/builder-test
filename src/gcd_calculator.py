from collections import Counter
from src.prime_factorization import prime_factorization

def prime_factorize(n: int) -> dict:
    """
    Convert prime factorization list to a dictionary of prime factors with their counts.
    
    Args:
        n (int): A positive integer to factorize
    
    Returns:
        dict: A dictionary with prime factors as keys and their counts as values
    """
    factors = prime_factorization(n)
    return dict(Counter(factors))

def gcd_using_prime_factors(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers using prime factorization.
    
    Args:
        a (int): First positive integer
        b (int): Second positive integer
    
    Returns:
        int: The Greatest Common Divisor of a and b
    
    Raises:
        ValueError: If either input is less than or equal to 0
    """
    # Validate input
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # Special case: if numbers are equal, return either
    if a == b:
        return a
    
    # Get prime factorizations
    a_factors = prime_factorize(a)
    b_factors = prime_factorize(b)
    
    # Calculate GCD by multiplying common prime factors
    gcd = 1
    for prime, count in a_factors.items():
        if prime in b_factors:
            # Take the minimum count of the common prime factors
            gcd *= prime ** min(count, b_factors[prime])
    
    return gcd