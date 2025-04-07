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
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Special case for 1
    if n == 1:
        return []
    
    # List to store prime factors
    factors = []
    
    # Start with the smallest prime factor, 2
    divisor = 2
    
    # Continue factoring while divisor squared is less than or equal to n
    while divisor * divisor <= n:
        # If divisor divides n evenly
        if n % divisor == 0:
            # Add divisor to factors
            factors.append(divisor)
            # Divide n by divisor
            n //= divisor
        else:
            # If current divisor doesn't divide n, move to next
            divisor += 1
    
    # If n is greater than 1, it means n is a prime factor itself
    if n > 1:
        factors.append(n)
    
    return factors