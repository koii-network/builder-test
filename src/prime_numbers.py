def find_primes_up_to_100():
    """
    Return a list of all prime numbers from 1 to 100.
    
    Returns:
        list: A sorted list of prime numbers between 1 and 100.
    """
    # Handle special cases
    if 1 >= 100:
        return []
    
    # Use the Sieve of Eratosthenes algorithm
    # Create a boolean array "is_prime[0..100]" and initialize
    # all entries it as true. A value in is_prime[i] will
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * 101
    is_prime[0] = is_prime[1] = False
    
    # Use Sieve of Eratosthenes
    for i in range(2, int(100**0.5) + 1):
        if is_prime[i]:
            # Update all multiples of i starting from i*i
            for j in range(i*i, 101, i):
                is_prime[j] = False
    
    # Collect prime numbers
    return [num for num in range(2, 101) if is_prime[num]]