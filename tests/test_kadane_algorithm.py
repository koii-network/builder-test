import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from kadane_algorithm import max_subarray_sum

def test_positive_numbers():
    """Test with an array of positive numbers."""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_numbers():
    """Test with a mix of positive and negative numbers."""
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_negative_numbers():
    """Test with an array of all negative numbers."""
    assert max_subarray_sum([-1, -2, -3, -4, -5]) == -1

def test_single_element():
    """Test with a single element array."""
    assert max_subarray_sum([42]) == 42

def test_zeros():
    """Test with an array containing zeros."""
    assert max_subarray_sum([0, 0, 0, 0]) == 0

def test_alternating_signs():
    """Test with an array of alternating positive and negative numbers."""
    assert max_subarray_sum([1, -1, 2, -2, 3, -3]) == 3

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError):
        max_subarray_sum("not a list")
    with pytest.raises(TypeError):
        max_subarray_sum(123)

def test_empty_list():
    """Test that a ValueError is raised for an empty list."""
    with pytest.raises(ValueError):
        max_subarray_sum([])