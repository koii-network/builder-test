import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from square_root import calculate_square_root

def test_positive_numbers():
    assert calculate_square_root(4) == 2.0
    assert calculate_square_root(9) == 3.0
    assert calculate_square_root(16) == 4.0

def test_zero():
    assert calculate_square_root(0) == 0.0

def test_float_numbers():
    assert pytest.approx(calculate_square_root(2), rel=1e-3) == 1.414

def test_negative_number_raises_error():
    with pytest.raises(ValueError, match="Cannot calculate square root of a negative number"):
        calculate_square_root(-4)

def test_invalid_input_raises_error():
    with pytest.raises(TypeError, match="Input must be a number"):
        calculate_square_root("not a number")
    with pytest.raises(TypeError, match="Input must be a number"):
        calculate_square_root(None)