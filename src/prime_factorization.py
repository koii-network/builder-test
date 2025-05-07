def prime_factorization(n):
    """
    Compute the prime factorization of a given positive integer.

    Args:
        n (int): A positive integer to factorize.

    Returns:
        list: A list of prime factors in ascending order.

    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    # Handle special cases
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if n == 0 or n == 1:
        return []
    
    # Prime factorization algorithm
    factors = []
    
    # Handle 2 as the first prime number
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Check for odd prime factors
    # We only need to check up to sqrt(n)
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors.append(factor)
            n = n // factor
        factor += 2
    
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return sorted(factors)