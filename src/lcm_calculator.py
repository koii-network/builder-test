from src.gcd_calculator import gcd

def lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of two integers.
    
    The LCM is calculated using the formula: LCM(a,b) = |a * b| / GCD(a,b)
    
    Args:
        a (int): First integer
        b (int): Second integer
    
    Returns:
        int: The Least Common Multiple of a and b
    
    Raises:
        ValueError: If either input is not a positive integer
        TypeError: If inputs are not integers
    """
    # Type checking
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    
    # Check for positive integers
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # Calculate LCM using the formula: LCM(a,b) = |a * b| / GCD(a,b)
    return abs(a * b) // gcd(a, b)

def lcm_multiple(*args: int) -> int:
    """
    Calculate the Least Common Multiple of multiple integers.
    
    Args:
        *args (int): Variable number of positive integers
    
    Returns:
        int: The Least Common Multiple of all input integers
    
    Raises:
        ValueError: If no arguments are provided or any argument is not a positive integer
        TypeError: If any input is not an integer
    """
    # Check if arguments are provided
    if len(args) == 0:
        raise ValueError("At least one integer is required")
    
    # Initialize result with the first number
    result = args[0]
    
    # Calculate LCM for all subsequent numbers
    for num in args[1:]:
        result = lcm(result, num)
    
    return result