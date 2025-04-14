from math import gcd

def simplify_fraction(numerator: int, denominator: int) -> tuple:
    """
    Simplify a fraction to its lowest terms.
    
    Args:
        numerator (int): The numerator of the fraction
        denominator (int): The denominator of the fraction
    
    Returns:
        tuple: A tuple containing the simplified numerator and denominator
    
    Raises:
        ValueError: If denominator is zero
        TypeError: If inputs are not integers
    """
    # Validate inputs
    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise TypeError("Numerator and denominator must be integers")
    
    # Check for zero denominator
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    
    # Handle special case of zero numerator
    if numerator == 0:
        return (0, 1)
    
    # Determine the sign 
    sign = 1
    if numerator * denominator < 0:
        sign = -1
    
    # Work with absolute values
    numerator = abs(numerator)
    denominator = abs(denominator)
    
    # Find the greatest common divisor
    divisor = gcd(numerator, denominator)
    
    # Simplify the fraction
    simplified_numerator = sign * (numerator // divisor)
    simplified_denominator = denominator // divisor
    
    return (simplified_numerator, simplified_denominator)