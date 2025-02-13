import pytest
import math
from src.square_root import calculate_square_root

def test_positive_numbers():
    # Test perfect squares
    assert math.isclose(calculate_square_root(4), 2, rel_tol=1e-9)
    assert math.isclose(calculate_square_root(9), 3, rel_tol=1e-9)
    assert math.isclose(calculate_square_root(16), 4, rel_tol=1e-9)
    
    # Test non-perfect squares
    assert math.isclose(calculate_square_root(2), math.sqrt(2), rel_tol=1e-9)
    assert math.isclose(calculate_square_root(7), math.sqrt(7), rel_tol=1e-9)

def test_zero():
    # Test zero
    assert calculate_square_root(0) == 0

def test_negative_number():
    # Test negative number raises ValueError
    with pytest.raises(ValueError, match="Cannot calculate square root of a negative number"):
        calculate_square_root(-4)

def test_invalid_input():
    # Test invalid input types
    with pytest.raises(TypeError, match="Input must be a number"):
        calculate_square_root("not a number")
    
    with pytest.raises(TypeError, match="Input must be a number"):
        calculate_square_root(None)
    
    with pytest.raises(TypeError, match="Input must be a number"):
        calculate_square_root([1, 2, 3])

def test_large_number():
    # Test a large number
    large_num = 10**10
    assert math.isclose(calculate_square_root(large_num), math.sqrt(large_num), rel_tol=1e-9)

def test_small_number():
    # Test a small number
    small_num = 0.01
    assert math.isclose(calculate_square_root(small_num), math.sqrt(small_num), rel_tol=1e-9)