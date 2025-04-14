import pytest
from src.array_flattener import flatten_array

def test_flatten_simple_list():
    """Test flattening a simple list"""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_nested_list():
    """Test flattening a nested list"""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list"""
    assert flatten_array([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_multiple_nested_levels():
    """Test flattening list with multiple nesting levels"""
    assert flatten_array([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_mixed_nesting():
    """Test flattening list with mixed nesting patterns"""
    assert flatten_array([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]

def test_flatten_empty_list():
    """Test flattening an empty list"""
    assert flatten_array([]) == []

def test_invalid_input_type():
    """Test that non-list inputs raise a TypeError"""
    with pytest.raises(TypeError):
        flatten_array("not a list")

def test_invalid_element_type():
    """Test that lists with non-numeric, non-list elements raise a TypeError"""
    with pytest.raises(TypeError):
        flatten_array([1, 2, "string"])

def test_float_support():
    """Test that float values are supported"""
    assert flatten_array([1.5, [2.7, 3], 4.2]) == [1.5, 2.7, 3, 4.2]