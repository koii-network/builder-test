"""
Basic Arithmetic Operations Module

This module provides simple arithmetic operations including addition, 
subtraction, multiplication, and division with error handling.
"""

def add(a: float, b: float) -> float:
    """
    Perform addition of two numbers.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Sum of a and b
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    Perform subtraction of two numbers.
    
    Args:
        a (float): Number to subtract from
        b (float): Number to subtract
    
    Returns:
        float: Result of a - b
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """
    Perform multiplication of two numbers.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Product of a and b
    """
    return a * b

def divide(a: float, b: float) -> float:
    """
    Perform division of two numbers.
    
    Args:
        a (float): Numerator
        b (float): Denominator
    
    Returns:
        float: Result of a divided by b
    
    Raises:
        ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b