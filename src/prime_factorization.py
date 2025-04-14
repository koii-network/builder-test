def prime_factorization(n):
    """
    Compute the prime factorization of a given positive integer.
    
    Args:
        n (int): A positive integer to factorize.
    
    Returns:
        list: A list of prime factors of the input number.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Special case for 1
    if n == 1:
        return []
    
    # List to store prime factors
    factors = []
    
    # Handle 2 as a special case first
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Check for odd prime factors
    factor = 3
    while factor * factor <= n:
        # If factor divides n, add it to factors
        while n % factor == 0:
            factors.append(factor)
            n //= factor
        # Move to next potential prime factor
        factor += 2
    
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return factors