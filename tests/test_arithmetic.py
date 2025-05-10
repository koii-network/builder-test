import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.arithmetic import add, subtract, multiply, divide

def test_add():
    """Test addition operation"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(1.5, 2.5) == 4.0

def test_add_error_handling():
    """Test error handling for add function"""
    with pytest.raises(TypeError):
        add("2", 3)
    with pytest.raises(TypeError):
        add(2, "3")
    with pytest.raises(TypeError):
        add(None, 3)

def test_subtract():
    """Test subtraction operation"""
    assert subtract(5, 3) == 2
    assert subtract(-1, 1) == -2
    assert subtract(4.5, 2.5) == 2.0

def test_subtract_error_handling():
    """Test error handling for subtract function"""
    with pytest.raises(TypeError):
        subtract("5", 3)
    with pytest.raises(TypeError):
        subtract(5, "3")
    with pytest.raises(TypeError):
        subtract(None, 3)

def test_multiply():
    """Test multiplication operation"""
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(1.5, 2) == 3.0

def test_multiply_error_handling():
    """Test error handling for multiply function"""
    with pytest.raises(TypeError):
        multiply("2", 3)
    with pytest.raises(TypeError):
        multiply(2, "3")
    with pytest.raises(TypeError):
        multiply(None, 3)

def test_divide():
    """Test division operation"""
    assert divide(6, 3) == 2
    assert divide(-6, 3) == -2
    assert divide(5, 2) == 2.5

def test_divide_error_handling():
    """Test error handling for divide function"""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
    with pytest.raises(TypeError):
        divide("6", 3)
    with pytest.raises(TypeError):
        divide(6, "3")
    with pytest.raises(TypeError):
        divide(None, 3)