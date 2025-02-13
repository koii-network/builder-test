import pytest
import math
from src.square_root import calculate_square_root

def test_positive_number_square_root():
    """Test square root calculation for positive numbers."""
    assert math.isclose(calculate_square_root(4), 2.0)
    assert math.isclose(calculate_square_root(9), 3.0)
    assert math.isclose(calculate_square_root(16), 4.0)

def test_zero_square_root():
    """Test square root of zero."""
    assert calculate_square_root(0) == 0.0

def test_float_square_root():
    """Test square root of float numbers."""
    assert math.isclose(calculate_square_root(2.25), 1.5)
    assert math.isclose(calculate_square_root(0.25), 0.5)

def test_large_number_square_root():
    """Test square root of large numbers."""
    assert math.isclose(calculate_square_root(1000000), 1000.0)

def test_negative_number_square_root():
    """Test that attempting to calculate square root of a negative number raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate square root of a negative number"):
        calculate_square_root(-4)

def test_negative_float_square_root():
    """Test that attempting to calculate square root of a negative float raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate square root of a negative number"):
        calculate_square_root(-2.5)