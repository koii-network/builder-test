import pytest
from src.list_sum import calculate_sum

def test_calculate_sum_normal_case():
    """Test with a standard list of integers."""
    test_list = [1, 2, 3, 4, 5]
    # Expected: 1*0 + 2*1 + 3*2 + 4*3 + 5*4 = 0 + 2 + 6 + 12 + 20 = 40
    assert calculate_sum(test_list) == 40

def test_calculate_sum_empty_list():
    """Test with an empty list."""
    assert calculate_sum([]) == 0

def test_calculate_sum_single_element():
    """Test with a single element list."""
    assert calculate_sum([10]) == 0

def test_calculate_sum_negative_numbers():
    """Test with negative numbers."""
    test_list = [-1, -2, -3, -4, -5]
    # Expected: -1*0 + -2*1 + -3*2 + -4*3 + -5*4 = 0 - 2 - 6 - 12 - 20 = -40
    assert calculate_sum(test_list) == -40

def test_calculate_sum_mixed_numbers():
    """Test with mixed positive and negative numbers."""
    test_list = [-1, 2, -3, 4, -5]
    # Expected: -1*0 + 2*1 + -3*2 + 4*3 + -5*4 = 0 + 2 - 6 + 12 - 20 = -12
    assert calculate_sum(test_list) == -12

def test_calculate_sum_non_list_input():
    """Test with non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_sum(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_sum("not a list")

def test_calculate_sum_non_integer_elements():
    """Test with non-integer elements in the list."""
    with pytest.raises(TypeError, match="All list elements must be integers"):
        calculate_sum([1, 2, "3", 4, 5])
    with pytest.raises(TypeError, match="All list elements must be integers"):
        calculate_sum([1.5, 2, 3, 4, 5])