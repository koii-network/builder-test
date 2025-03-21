import pytest
from src.list_sum import calculate_sum

def test_calculate_sum_normal_case():
    """Test with a standard list of integers."""
    test_list = [1, 2, 3, 4, 5]
    assert calculate_sum(test_list) == 40  # 0*1 + 1*2 + 2*3 + 3*4 + 4*5 = 40

def test_calculate_sum_empty_list():
    """Test with an empty list."""
    assert calculate_sum([]) == 0

def test_calculate_sum_single_element():
    """Test with a single-element list."""
    assert calculate_sum([10]) == 0

def test_calculate_sum_negative_numbers():
    """Test with negative numbers."""
    test_list = [-1, -2, -3, -4, -5]
    assert calculate_sum(test_list) == -40

def test_calculate_sum_mixed_numbers():
    """Test with mixed positive and negative numbers."""
    test_list = [-1, 2, -3, 4, -5]
    assert calculate_sum(test_list) == -12  # Corrected expected value

def test_calculate_sum_invalid_input_not_list():
    """Test with non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_sum("not a list")

def test_calculate_sum_invalid_input_non_integers():
    """Test with list containing non-integer elements."""
    with pytest.raises(TypeError, match="All list elements must be integers"):
        calculate_sum([1, 2, "3", 4, 5])

def test_calculate_sum_zero_values():
    """Test with a list containing zero values."""
    test_list = [0, 0, 0, 0, 0]
    assert calculate_sum(test_list) == 0