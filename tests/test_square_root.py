import pytest
import math
from src.square_root import calculate_square_root

def test_positive_numbers():
    assert math.isclose(calculate_square_root(4), 2, rel_tol=1e-9)
    assert math.isclose(calculate_square_root(9), 3, rel_tol=1e-9)
    assert math.isclose(calculate_square_root(16), 4, rel_tol=1e-9)

def test_zero():
    assert calculate_square_root(0) == 0

def test_large_number():
    assert math.isclose(calculate_square_root(1000000), 1000, rel_tol=1e-9)

def test_decimal_number():
    assert math.isclose(calculate_square_root(2), math.sqrt(2), rel_tol=1e-9)

def test_negative_number():
    with pytest.raises(ValueError, match="Cannot calculate square root of a negative number"):
        calculate_square_root(-4)

def test_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be a number"):
        calculate_square_root("not a number")
    
    with pytest.raises(TypeError, match="Input must be a number"):
        calculate_square_root([1, 2, 3])