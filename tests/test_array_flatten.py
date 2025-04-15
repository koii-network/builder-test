import pytest
from src.array_flatten import flatten_array

def test_flatten_single_level_array():
    """Test flattening a single-level array"""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_nested_array():
    """Test flattening a nested array"""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_deeply_nested_array():
    """Test flattening a deeply nested array"""
    assert flatten_array([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_empty_array():
    """Test flattening an empty array"""
    assert flatten_array([]) == []

def test_flatten_array_with_empty_nested_lists():
    """Test flattening an array with empty nested lists"""
    assert flatten_array([1, [], [2, []], 3]) == [1, 2, 3]

def test_invalid_element_type():
    """Test raising TypeError for non-integer and non-list elements"""
    with pytest.raises(TypeError, match="Invalid element type"):
        flatten_array([1, 2, "3"])

def test_complex_nested_array():
    """Test flattening a complex nested array"""
    assert flatten_array([1, [2, [3, [4, 5]]], [6, 7]]) == [1, 2, 3, 4, 5, 6, 7]