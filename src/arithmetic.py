def add(a, b):
    """
    Perform addition of two numbers.
    
    Args:
        a (int or float): First number
        b (int or float): Second number
    
    Returns:
        int or float: Sum of a and b
    
    Raises:
        TypeError: If inputs are not numbers
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Inputs must be numbers")
    return a + b

def subtract(a, b):
    """
    Perform subtraction of two numbers.
    
    Args:
        a (int or float): Number to subtract from
        b (int or float): Number to subtract
    
    Returns:
        int or float: Difference between a and b
    
    Raises:
        TypeError: If inputs are not numbers
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Inputs must be numbers")
    return a - b

def multiply(a, b):
    """
    Perform multiplication of two numbers.
    
    Args:
        a (int or float): First number
        b (int or float): Second number
    
    Returns:
        int or float: Product of a and b
    
    Raises:
        TypeError: If inputs are not numbers
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Inputs must be numbers")
    return a * b

def divide(a, b):
    """
    Perform division of two numbers.
    
    Args:
        a (int or float): Dividend
        b (int or float): Divisor
    
    Returns:
        float: Quotient of a divided by b
    
    Raises:
        TypeError: If inputs are not numbers
        ZeroDivisionError: If b is zero
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Inputs must be numbers")
    
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    
    return a / b