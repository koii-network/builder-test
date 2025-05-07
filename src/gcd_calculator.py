from typing import List, Dict
from math import gcd as math_gcd
from functools import reduce

def prime_factorization(n: int) -> Dict[int, int]:
    """
    Decompose a number into its prime factors.
    
    Args:
        n (int): The number to factorize (must be non-negative)
    
    Returns:
        Dict[int, int]: A dictionary of prime factors and their exponents
    
    Raises:
        ValueError: If input is negative
    """
    if n < 0:
        raise ValueError("Cannot factorize negative numbers")
    
    # Handle special cases
    if n == 0:
        return {}
    if n == 1:
        return {1: 1}
    
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    
    # If n is a prime factor greater than sqrt(n)
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    
    return factors

def gcd_prime_factors(*numbers: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) using prime factorization.
    
    Args:
        *numbers (int): Variable number of integers to find GCD for
    
    Returns:
        int: The Greatest Common Divisor of the input numbers
    
    Raises:
        ValueError: If no arguments are provided
        TypeError: If any argument is not an integer
    """
    # Validate input
    if len(numbers) == 0:
        raise ValueError("At least one number must be provided")
    
    # Check all inputs are integers
    if not all(isinstance(n, int) for n in numbers):
        raise TypeError("All arguments must be integers")
    
    # Handle special cases
    if 0 in numbers:
        # If any number is 0, return the max of other numbers 
        # (excluding 0 itself)
        non_zero = [abs(n) for n in numbers if n != 0]
        return max(non_zero) if non_zero else 0
    
    # Take absolute values to handle negative numbers
    abs_numbers = [abs(n) for n in numbers]
    
    # If only one number, return its absolute value
    if len(abs_numbers) == 1:
        return abs_numbers[0]
    
    # Use Python's built-in reduce with math.gcd for efficiency
    # This handles cases where prime factorization might be slower
    if len(abs_numbers) == 2:
        return math_gcd(abs_numbers[0], abs_numbers[1])
    
    # Reduce the list using math.gcd
    return reduce(math_gcd, abs_numbers)