import pytest
from src.sum_calculator import calculate_sum

def test_calculate_sum_basic():
    """Test basic sum calculation with index multiplication."""
    test_list = [1, 2, 3, 4]
    # Expected: (1*0) + (2*1) + (3*2) + (4*3) = 0 + 2 + 6 + 12 = 20
    assert calculate_sum(test_list) == 20

def test_calculate_sum_empty_list():
    """Test sum calculation with an empty list."""
    assert calculate_sum([]) == 0

def test_calculate_sum_single_element():
    """Test sum calculation with a single element."""
    assert calculate_sum([5]) == 0

def test_calculate_sum_negative_numbers():
    """Test sum calculation with negative numbers."""
    test_list = [-1, -2, -3, -4]
    # Expected: (-1*0) + (-2*1) + (-3*2) + (-4*3) = 0 - 2 - 6 - 12 = -20
    assert calculate_sum(test_list) == -20

def test_calculate_sum_non_list_input():
    """Test error handling for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_sum(123)

def test_calculate_sum_non_integer_input():
    """Test error handling for list with non-integer elements."""
    with pytest.raises(TypeError, match="List must contain only integers"):
        calculate_sum([1, 2, '3', 4])