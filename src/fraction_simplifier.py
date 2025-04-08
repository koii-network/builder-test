from math import gcd

def simplify_fraction(numerator: int, denominator: int) -> tuple[int, int]:
    """
    Simplify a fraction to its lowest terms.

    Args:
        numerator (int): The numerator of the fraction.
        denominator (int): The denominator of the fraction.

    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator.

    Raises:
        ValueError: If the denominator is zero.
        TypeError: If non-integer inputs are provided.
    """
    # Type checking
    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise TypeError("Numerator and denominator must be integers")
    
    # Check for zero denominator
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    
    # Handle sign normalization
    # Ensure the negative sign is always on the numerator
    if denominator < 0:
        numerator = -numerator
        denominator = abs(denominator)
    
    # Find the greatest common divisor and simplify
    divisor = gcd(abs(numerator), abs(denominator))
    
    return (numerator // divisor, denominator // divisor)