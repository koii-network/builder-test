from src.gcd_calculator import gcd_using_prime_factors as gcd

def lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of two integers using the GCD method.
    
    The LCM is calculated using the formula: LCM(a,b) = |a * b| / GCD(a,b)
    
    Args:
        a (int): First integer
        b (int): Second integer
    
    Returns:
        int: The least common multiple of a and b
    
    Raises:
        ValueError: If either input is not a positive integer
    """
    # Validate inputs are positive integers
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Both inputs must be integers")
    
    if a < 0 or b < 0:
        raise ValueError("Both inputs must be non-negative integers")
    
    # Special case: if either number is 0, return 0
    if a == 0 or b == 0:
        return 0
    
    # Calculate LCM using the GCD method
    return abs(a * b) // gcd(a, b)

def lcm_multiple(*numbers: int) -> int:
    """
    Calculate the LCM of multiple integers.
    
    Args:
        *numbers (int): Variable number of non-negative integers
    
    Returns:
        int: The least common multiple of all input numbers
    
    Raises:
        ValueError: If no numbers are provided or if any input is invalid
    """
    if not numbers:
        raise ValueError("At least one number must be provided")
    
    # Start with the first number
    result = numbers[0]
    
    # Iteratively calculate LCM for all numbers
    for num in numbers[1:]:
        result = lcm(result, num)
    
    return result