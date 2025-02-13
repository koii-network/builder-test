import pytest
import math
from src.square_root import calculate_square_root

def test_positive_numbers():
    """Test square root calculation for positive numbers."""
    assert math.isclose(calculate_square_root(4), 2, rel_tol=1e-9)
    assert math.isclose(calculate_square_root(9), 3, rel_tol=1e-9)
    assert math.isclose(calculate_square_root(16), 4, rel_tol=1e-9)
    assert math.isclose(calculate_square_root(0.25), 0.5, rel_tol=1e-9)

def test_zero():
    """Test square root of zero."""
    assert calculate_square_root(0) == 0

def test_one():
    """Test square root of one."""
    assert math.isclose(calculate_square_root(1), 1, rel_tol=1e-9)

def test_negative_number():
    """Test that negative numbers raise a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate square root of a negative number"):
        calculate_square_root(-4)

def test_invalid_input():
    """Test that non-numeric inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a number"):
        calculate_square_root("not a number")
    with pytest.raises(TypeError, match="Input must be a number"):
        calculate_square_root(None)
    with pytest.raises(TypeError, match="Input must be a number"):
        calculate_square_root([1, 2, 3])

def test_large_number():
    """Test square root calculation for a large number."""
    assert math.isclose(calculate_square_root(10000), 100, rel_tol=1e-9)

def test_small_number():
    """Test square root calculation for a small number."""
    assert math.isclose(calculate_square_root(0.01), 0.1, rel_tol=1e-9)