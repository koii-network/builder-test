from src.gcd_calculator import gcd_with_prime_factors

def lcm_with_gcd(a, b):
    """
    Calculate the Least Common Multiple (LCM) of two numbers using GCD.
    
    This function uses the formula: LCM(a,b) = |a * b| / GCD(a,b)
    
    Args:
        a (int): First positive integer.
        b (int): Second positive integer.
    
    Returns:
        int: The Least Common Multiple of a and b.
    
    Raises:
        TypeError: If inputs are not integers.
        ValueError: If inputs are not positive integers.
    """
    # Input validation
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Inputs must be integers")
    
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # Calculate GCD
    gcd = gcd_with_prime_factors(a, b)
    
    # Calculate LCM using the formula: LCM(a,b) = |a * b| / GCD(a,b)
    return abs(a * b) // gcd