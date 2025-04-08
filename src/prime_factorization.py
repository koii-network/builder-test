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
    
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Special case for 1
    if n == 1:
        return []
    
    # List to store prime factors
    factors = []
    
    # Start with the smallest prime number
    divisor = 2
    
    # Continue factoring while divisor squared is less than or equal to n
    while divisor * divisor <= n:
        # If divisor divides n evenly
        if n % divisor == 0:
            # Add the divisor to factors
            factors.append(divisor)
            # Divide n by the divisor
            n //= divisor
        else:
            # If not divisible, increment divisor
            divisor += 1
    
    # If n is greater than 1, it is a prime factor itself
    if n > 1:
        factors.append(n)
    
    return factors