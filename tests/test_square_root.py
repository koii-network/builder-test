import pytest
import math
from src.square_root import calculate_square_root

def test_positive_numbers():
    # Test basic square roots
    assert math.isclose(calculate_square_root(4), 2, rel_tol=1e-10)
    assert math.isclose(calculate_square_root(9), 3, rel_tol=1e-10)
    assert math.isclose(calculate_square_root(16), 4, rel_tol=1e-10)

def test_zero():
    # Test zero input
    assert calculate_square_root(0) == 0

def test_one():
    # Test perfect square
    assert calculate_square_root(1) == 1

def test_float_input():
    # Test floating point numbers
    assert math.isclose(calculate_square_root(2.0), math.sqrt(2), rel_tol=1e-10)
    assert math.isclose(calculate_square_root(3.14), math.sqrt(3.14), rel_tol=1e-10)

def test_negative_input():
    # Test negative number raises ValueError
    with pytest.raises(ValueError, match="Cannot calculate square root of a negative number"):
        calculate_square_root(-4)

def test_invalid_input():
    # Test invalid input types
    with pytest.raises(TypeError, match="Input must be a number"):
        calculate_square_root("not a number")
    with pytest.raises(TypeError, match="Input must be a number"):
        calculate_square_root([1, 2, 3])
    with pytest.raises(TypeError, match="Input must be a number"):
        calculate_square_root(None)