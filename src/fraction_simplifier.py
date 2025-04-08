from src.gcd_calculator import gcd

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
        TypeError: If inputs are not integers.
    """
    # Check input types
    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise TypeError("Numerator and denominator must be integers")

    # Check for zero denominator
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")

    # Handle special case of zero numerator
    if numerator == 0:
        return 0, 1

    # Ensure correct sign handling
    sign = 1
    if numerator * denominator < 0:
        sign = -1

    # Take absolute values for GCD calculation
    abs_numerator = abs(numerator)
    abs_denominator = abs(denominator)

    # Calculate the greatest common divisor
    divisor = gcd(abs_numerator, abs_denominator)

    # Simplify the fraction
    simplified_numerator = sign * (abs_numerator // divisor)
    simplified_denominator = abs_denominator // divisor

    return simplified_numerator, simplified_denominator