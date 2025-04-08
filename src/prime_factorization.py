def prime_factorization(n):
    """
    Compute the prime factorization of a given positive integer.
    
    Args:
        n (int): A positive integer to factorize.
    
    Returns:
        list: A list of prime factors, with possible repetitions.
    
    Raises:
        ValueError: If the input is less than 2.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        raise ValueError("Input must be 2 or greater")
    
    # List to store prime factors
    factors = []
    
    # Start with the smallest prime number
    divisor = 2
    
    # Continue factoring until n becomes 1
    while divisor * divisor <= n:
        if n % divisor == 0:
            # If divisor divides n, add it to factors and divide n
            factors.append(divisor)
            n //= divisor
        else:
            # Move to next potential divisor
            divisor += 1
    
    # If n is still greater than 1, it means n is a prime factor itself
    if n > 1:
        factors.append(n)
    
    return factors