from src.gcd_calculator import gcd_using_prime_factors
from math import gcd

def lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of two positive integers using GCD.
    
    LCM is calculated using the formula: LCM(a,b) = (a * b) / GCD(a,b)
    
    Args:
        a (int): First non-negative integer
        b (int): Second non-negative integer
    
    Returns:
        int: The Least Common Multiple of a and b
    
    Raises:
        ValueError: If either input is negative
    """
    # Validate input
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers")
    
    # Special case: if either number is 0, LCM is 0
    if a == 0 or b == 0:
        return 0
    
    # Use Python's built-in gcd for better performance with large numbers
    # Calculate LCM using the formula: LCM(a,b) = (a * b) / GCD(a,b)
    return (a * b) // gcd(a, b)

def lcm_multiple(*numbers: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of multiple non-negative integers.
    
    Args:
        *numbers (int): Variable number of non-negative integers
    
    Returns:
        int: The Least Common Multiple of all input numbers
    
    Raises:
        ValueError: If no numbers are provided or any number is negative
    """
    if not numbers:
        raise ValueError("At least one number must be provided")
    
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    
    return result