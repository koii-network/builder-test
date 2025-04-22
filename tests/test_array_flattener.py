import pytest
from src.array_flattener import flatten_array

def test_flatten_simple_list():
    """Test flattening a simple list with no nested lists"""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_single_nested_list():
    """Test flattening a list with one level of nesting"""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_multiple_nested_lists():
    """Test flattening a list with multiple levels of nesting"""
    assert flatten_array([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list"""
    assert flatten_array([1, [2, [3, [4, [5]]]], 6]) == [1, 2, 3, 4, 5, 6]

def test_flatten_empty_list():
    """Test flattening an empty list"""
    assert flatten_array([]) == []

def test_flatten_nested_empty_lists():
    """Test flattening a list with nested empty lists"""
    assert flatten_array([1, [], [2, []], 3]) == [1, 2, 3]

def test_invalid_input_non_list():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_array(123)

def test_invalid_input_non_integer_element():
    """Test that a TypeError is raised for non-integer/non-list elements"""
    with pytest.raises(TypeError):
        flatten_array([1, 2, "3"])
    with pytest.raises(TypeError):
        flatten_array([1, [2, 3.14], 4])

def test_flatten_single_element_list():
    """Test flattening a list with a single element"""
    assert flatten_array([42]) == [42]

def test_flatten_list_with_single_nested_list():
    """Test flattening a list containing a single nested list"""
    assert flatten_array([[1]]) == [1]