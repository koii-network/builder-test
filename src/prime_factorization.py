from collections import Counter
from src.prime_utils import is_prime

def prime_factorization(n):
    """
    Compute the prime factorization of a given positive integer.
    
    Args:
        n (int): A positive integer to factorize.
    
    Returns:
        dict: A dictionary where keys are prime factors and values are their frequencies.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Special case for 1
    if n == 1:
        return {}
    
    # List to store prime factors
    factors = []
    
    # Start with the smallest prime factor, 2
    divisor = 2
    
    # Continue factoring while divisor squared is less than or equal to n
    while divisor * divisor <= n:
        # If divisor divides n evenly
        if n % divisor == 0:
            # Verify that divisor is prime
            if not is_prime(divisor):
                raise ValueError(f"Unexpected non-prime divisor: {divisor}")
            
            # Add divisor to factors
            factors.append(divisor)
            # Divide n by divisor
            n //= divisor
        else:
            # If current divisor doesn't divide n, move to next
            divisor += 1
    
    # If n is greater than 1, it means n is a prime factor itself
    if n > 1:
        if not is_prime(n):
            raise ValueError(f"Unexpected non-prime factor: {n}")
        factors.append(n)
    
    # Return a dictionary with prime factors and their frequencies
    return dict(Counter(factors))