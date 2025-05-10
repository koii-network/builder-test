"""
Unit tests for arithmetic operations module.
"""

import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.arithmetic import add, subtract, multiply, divide

def test_add():
    """Test addition operation."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0

def test_subtract():
    """Test subtraction operation."""
    assert subtract(5, 3) == 2
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0
    assert subtract(3.5, 1.5) == 2.0

def test_multiply():
    """Test multiplication operation."""
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0
    assert multiply(1.5, 2) == 3.0

def test_divide():
    """Test division operation."""
    assert divide(6, 3) == 2
    assert divide(-6, 2) == -3
    assert divide(0, 5) == 0
    assert divide(5.0, 2) == 2.5

def test_divide_by_zero():
    """Test division by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(5, 0)

def test_floating_point_precision():
    """Test floating point arithmetic precision."""
    assert abs(divide(1, 3) - 0.3333333) < 1e-6