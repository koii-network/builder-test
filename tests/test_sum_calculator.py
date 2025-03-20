import pytest
from src.sum_calculator import calculate_sum

def test_calculate_sum_normal_case():
    """Test with a normal list of integers"""
    assert calculate_sum([1, 2, 3, 4]) == (1*0 + 2*1 + 3*2 + 4*3)

def test_calculate_sum_empty_list():
    """Test with an empty list"""
    assert calculate_sum([]) == 0

def test_calculate_sum_single_element():
    """Test with a single element list"""
    assert calculate_sum([5]) == 0

def test_calculate_sum_negative_numbers():
    """Test with negative numbers"""
    assert calculate_sum([-1, -2, -3]) == (-1*0 + -2*1 + -3*2)

def test_calculate_sum_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    assert calculate_sum([1, -2, 3, -4]) == (1*0 + -2*1 + 3*2 + -4*3)

def test_calculate_sum_invalid_input_non_list():
    """Test with non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_sum("not a list")

def test_calculate_sum_invalid_input_non_integers():
    """Test with list containing non-integer elements"""
    with pytest.raises(TypeError, match="All list elements must be integers"):
        calculate_sum([1, 2, "3", 4])