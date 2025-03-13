import pytest
from src.list_sum_calculator import calculate_sum

def test_calculate_sum_basic():
    """Test basic functionality with a simple list."""
    assert calculate_sum([1, 2, 3]) == 8  # 0*1 + 1*2 + 2*3 = 0 + 2 + 6 = 8

def test_calculate_sum_empty_list():
    """Test with an empty list."""
    assert calculate_sum([]) == 0

def test_calculate_sum_single_element():
    """Test with a single element list."""
    assert calculate_sum([5]) == 0  # 0*5 = 0

def test_calculate_sum_negative_numbers():
    """Test with negative numbers."""
    assert calculate_sum([-1, -2, -3]) == -14  # 0*(-1) + 1*(-2) + 2*(-3) = 0 - 2 - 6 = -8

def test_calculate_sum_mixed_numbers():
    """Test with a mix of positive and negative numbers."""
    assert calculate_sum([-1, 2, -3, 4]) == 10  # 0*(-1) + 1*2 + 2*(-3) + 3*4 = 0 + 2 - 6 + 12 = 8

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_sum("not a list")

def test_invalid_element_type():
    """Test that a TypeError is raised for non-integer elements."""
    with pytest.raises(TypeError, match="All list elements must be integers"):
        calculate_sum([1, 2, "3", 4])