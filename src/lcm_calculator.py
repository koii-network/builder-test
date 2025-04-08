from src.gcd_calculator import gcd_using_prime_factors

def lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of two positive integers using GCD.
    
    LCM is calculated using the formula: LCM(a,b) = (a * b) / GCD(a,b)
    
    Args:
        a (int): First positive integer
        b (int): Second positive integer
    
    Returns:
        int: The Least Common Multiple of a and b
    
    Raises:
        ValueError: If either input is less than or equal to 0
    """
    # Validate input
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # Special case: if either number is 0, LCM is 0
    if a == 0 or b == 0:
        return 0
    
    # Use the formula: LCM(a,b) = (a * b) / GCD(a,b)
    # Use integer division to handle large numbers efficiently
    gcd = gcd_using_prime_factors(a, b)
    return (a * b) // gcd

def lcm_multiple(*numbers: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of multiple positive integers.
    
    Args:
        *numbers (int): Variable number of positive integers
    
    Returns:
        int: The Least Common Multiple of all input numbers
    
    Raises:
        ValueError: If no numbers are provided or any number is less than or equal to 0
    """
    if not numbers:
        raise ValueError("At least one number must be provided")
    
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    
    return result