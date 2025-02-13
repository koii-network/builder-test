import pytest
import math
from src.square_root import calculate_square_root

def test_positive_number_square_root():
    """Test square root of positive numbers."""
    assert math.isclose(calculate_square_root(4), 2.0, rel_tol=1e-9)
    assert math.isclose(calculate_square_root(9), 3.0, rel_tol=1e-9)
    assert math.isclose(calculate_square_root(16), 4.0, rel_tol=1e-9)

def test_zero_square_root():
    """Test square root of zero."""
    assert calculate_square_root(0) == 0

def test_one_square_root():
    """Test square root of one."""
    assert calculate_square_root(1) == 1.0

def test_decimal_square_root():
    """Test square root of decimal numbers."""
    assert math.isclose(calculate_square_root(2.25), 1.5, rel_tol=1e-9)
    assert math.isclose(calculate_square_root(0.16), 0.4, rel_tol=1e-9)

def test_negative_number_raises_error():
    """Test that calculating square root of negative number raises ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate square root of a negative number"):
        calculate_square_root(-4)

def test_non_numeric_input_raises_error():
    """Test that non-numeric input raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a number"):
        calculate_square_root("not a number")
    with pytest.raises(TypeError, match="Input must be a number"):
        calculate_square_root(None)
    with pytest.raises(TypeError, match="Input must be a number"):
        calculate_square_root([1, 2, 3])