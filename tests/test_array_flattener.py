import pytest
from src.array_flattener import flatten_array

def test_flatten_simple_list():
    """Test flattening a simple list with nested elements."""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list."""
    assert flatten_array([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_empty_list():
    """Test flattening an empty list."""
    assert flatten_array([]) == []

def test_flatten_list_with_empty_sublists():
    """Test flattening a list with empty sublists."""
    assert flatten_array([1, [], [2, []], 3]) == [1, 2, 3]

def test_flatten_multiple_levels_of_nesting():
    """Test flattening multiple levels of nested lists."""
    assert flatten_array([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_list_with_non_integer_elements():
    """Test flattening a list with non-integer elements (should ignore them)."""
    assert flatten_array([1, [2, 'a', 3], 4.5, [5]]) == [1, 2, 3, 5]

def test_flatten_single_element_list():
    """Test flattening a single-element list."""
    assert flatten_array([42]) == [42]

def test_flatten_complex_nested_structure():
    """Test flattening a complex nested structure."""
    assert flatten_array([1, [2, [3, [4, [5]]], 6], 7]) == [1, 2, 3, 4, 5, 6, 7]