from src.is_prime import is_prime

def prime_factorization(n):
    """
    Compute the prime factorization of a given positive integer.
    
    Args:
        n (int): A positive integer to factorize.
    
    Returns:
        list: A list of prime factors in ascending order.
    
    Raises:
        ValueError: If the input is less than 2.
        TypeError: If the input is not an integer.
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        raise ValueError("Input must be a positive integer greater than or equal to 2")
    
    # List to store prime factors
    factors = []
    
    # Special case for 2
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Check for odd prime factors
    factor = 3
    while factor * factor <= n:
        # Ensure only prime factors are added
        if is_prime(factor):
            # If factor divides n, add it to factors
            while n % factor == 0:
                factors.append(factor)
                n = n // factor
        # Move to next potential prime factor
        factor += 2
    
    # If n is a prime number greater than 2
    if n > 2 and is_prime(n):
        factors.append(n)
    
    return factors