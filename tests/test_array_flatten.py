import pytest
from src.array_flatten import flatten_array

def test_flatten_simple_list():
    """Test flattening a simple list"""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_nested_list():
    """Test flattening a list with one level of nesting"""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_deeply_nested_list():
    """Test flattening a list with multiple levels of nesting"""
    assert flatten_array([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_empty_list():
    """Test flattening an empty list"""
    assert flatten_array([]) == []

def test_flatten_list_with_empty_sublists():
    """Test flattening a list with empty sublists"""
    assert flatten_array([1, [], [2, []], 3]) == [1, 2, 3]

def test_invalid_type_raises_error():
    """Test that non-integer, non-list elements raise a TypeError"""
    with pytest.raises(TypeError):
        flatten_array([1, 2, "3"])

def test_nested_invalid_type_raises_error():
    """Test that nested invalid types also raise a TypeError"""
    with pytest.raises(TypeError):
        flatten_array([1, [2, "3"], 4])

def test_multiple_nested_levels():
    """Test flattening a list with multiple nested levels"""
    assert flatten_array([1, [2, [3, [4, 5]]], 6]) == [1, 2, 3, 4, 5, 6]