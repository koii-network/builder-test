import pytest
from src.list_sum import calculate_sum

def test_calculate_sum_normal_case():
    """Test with a typical list of integers."""
    assert calculate_sum([1, 2, 3, 4]) == 20  # 0*1 + 1*2 + 2*3 + 3*4 = 0 + 2 + 6 + 12 = 20

def test_calculate_sum_empty_list():
    """Test with an empty list."""
    assert calculate_sum([]) == 0

def test_calculate_sum_single_element():
    """Test with a single element list."""
    assert calculate_sum([5]) == 0

def test_calculate_sum_negative_numbers():
    """Test with negative numbers."""
    assert calculate_sum([-1, -2, -3]) == -14  # 0*(-1) + 1*(-2) + 2*(-3) = 0 - 2 - 6 = -8

def test_calculate_sum_zero_numbers():
    """Test with a list containing zeros."""
    assert calculate_sum([0, 0, 0]) == 0

def test_calculate_sum_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_sum("not a list")

def test_calculate_sum_invalid_list_elements():
    """Test that a TypeError is raised for list with non-integer elements."""
    with pytest.raises(TypeError, match="List must contain only integers"):
        calculate_sum([1, 2, "3", 4])