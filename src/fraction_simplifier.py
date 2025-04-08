from src.gcd_calculator import calculate_gcd

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
        TypeError: If numerator or denominator are not integers.
    """
    # Validate input types
    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise TypeError("Numerator and denominator must be integers")

    # Check for zero denominator
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")

    # Handle zero numerator case
    if numerator == 0:
        return 0, 1

    # Determine sign
    sign = 1
    if numerator < 0 and denominator < 0:
        sign = 1
    elif numerator < 0 or denominator < 0:
        sign = -1

    # Take absolute values for GCD calculation
    abs_numerator = abs(numerator)
    abs_denominator = abs(denominator)

    # Calculate GCD
    gcd = calculate_gcd(abs_numerator, abs_denominator)

    # Simplify the fraction
    simplified_numerator = sign * (abs_numerator // gcd)
    simplified_denominator = abs_denominator // gcd

    return simplified_numerator, simplified_denominator