import pytest
from src.list_utils import calculate_sum

def test_calculate_sum_basic():
    """Test basic sum with index weighting"""
    assert calculate_sum([1, 2, 3]) == 8  # 0*1 + 1*2 + 2*3 = 0 + 2 + 6 = 8

def test_calculate_sum_empty_list():
    """Test sum of an empty list"""
    assert calculate_sum([]) == 0

def test_calculate_sum_negative_numbers():
    """Test sum with negative numbers"""
    assert calculate_sum([-1, -2, -3]) == -8  # 0*(-1) + 1*(-2) + 2*(-3) = 0 - 2 - 6 = -8

def test_calculate_sum_mixed_numbers():
    """Test sum with mixed numbers"""
    assert calculate_sum([1, -2, 3, -4]) == -8  # 0*1 + 1*(-2) + 2*3 + 3*(-4) = 0 - 2 + 6 - 12 = -8

def test_calculate_sum_invalid_input_type():
    """Test that a type error is raised for non-list inputs"""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_sum("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_sum(123)

def test_calculate_sum_invalid_list_elements():
    """Test that a type error is raised for lists with non-integer elements"""
    with pytest.raises(TypeError, match="All list elements must be integers"):
        calculate_sum([1, 2, "3"])
    with pytest.raises(TypeError, match="All list elements must be integers"):
        calculate_sum([1, 2.5, 3])