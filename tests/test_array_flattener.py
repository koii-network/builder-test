import pytest
from src.array_flattener import flatten_array

def test_flatten_simple_nested_list():
    """Test flattening a simple nested list."""
    input_list = [1, [2, 3], 4]
    assert flatten_array(input_list) == [1, 2, 3, 4]

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list."""
    input_list = [1, [2, [3, 4]], [5, [6, 7]]]
    assert flatten_array(input_list) == [1, 2, 3, 4, 5, 6, 7]

def test_flatten_empty_list():
    """Test flattening an empty list."""
    assert flatten_array([]) == []

def test_flatten_no_nesting():
    """Test flattening a list with no nesting."""
    input_list = [1, 2, 3, 4, 5]
    assert flatten_array(input_list) == [1, 2, 3, 4, 5]

def test_flatten_mixed_types():
    """Test flattening a list with mixed types and nesting."""
    input_list = [1, 'a', [2, 'b'], [3, [4, 'c']]]
    assert flatten_array(input_list) == [1, 'a', 2, 'b', 3, 4, 'c']

def test_flatten_single_element_lists():
    """Test flattening lists with single-element nested lists."""
    input_list = [[1], [2], [3]]
    assert flatten_array(input_list) == [1, 2, 3]