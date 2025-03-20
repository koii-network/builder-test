import pytest
from src.sum_calculator import calculate_sum

def test_calculate_sum_basic():
    """Test basic functionality with simple list of integers."""
    assert calculate_sum([1, 2, 3, 4]) == 20  # 0*1 + 1*2 + 2*3 + 3*4 = 20

def test_calculate_sum_empty_list():
    """Test behavior with an empty list."""
    assert calculate_sum([]) == 0

def test_calculate_sum_single_element():
    """Test behavior with a single-element list."""
    assert calculate_sum([5]) == 0

def test_calculate_sum_negative_numbers():
    """Test behavior with negative numbers."""
    assert calculate_sum([-1, -2, -3]) == -8  # 0*(-1) + 1*(-2) + 2*(-3)

def test_calculate_sum_mixed_numbers():
    """Test behavior with mixed positive and negative numbers."""
    assert calculate_sum([1, -2, 3, -4]) == -8  # 0*1 + 1*(-2) + 2*3 + 3*(-4)

def test_calculate_sum_invalid_input_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_sum("not a list")

def test_calculate_sum_invalid_list_elements():
    """Test that TypeError is raised for list with non-integer elements."""
    with pytest.raises(TypeError, match="All list elements must be integers"):
        calculate_sum([1, 2, "3", 4])