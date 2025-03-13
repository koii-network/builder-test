import pytest
from src.list_sum import calculate_sum

def test_calculate_sum_basic():
    """Test basic functionality with a simple list."""
    assert calculate_sum([1, 2, 3]) == 8  # 0*1 + 1*2 + 2*3 = 0 + 2 + 6 = 8

def test_calculate_sum_empty_list():
    """Test with an empty list."""
    assert calculate_sum([]) == 0

def test_calculate_sum_negative_numbers():
    """Test with negative numbers."""
    assert calculate_sum([-1, -2, -3]) == -8  # 0*(-1) + 1*(-2) + 2*(-3) = 0 - 2 - 6 = -8

def test_calculate_sum_zero_list():
    """Test with a list of zeros."""
    assert calculate_sum([0, 0, 0]) == 0

def test_calculate_sum_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_sum("not a list")

def test_calculate_sum_invalid_element_type():
    """Test raising TypeError for non-integer list elements."""
    with pytest.raises(TypeError, match="All list elements must be integers"):
        calculate_sum([1, 2, "3"])