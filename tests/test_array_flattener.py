import pytest
from src.array_flattener import flatten_array

def test_simple_array():
    """Test flattening a simple array"""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_nested_array():
    """Test flattening a nested array"""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_deeply_nested_array():
    """Test flattening a deeply nested array"""
    assert flatten_array([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_empty_array():
    """Test flattening an empty array"""
    assert flatten_array([]) == []

def test_none_input():
    """Test flattening None input"""
    assert flatten_array(None) == []

def test_multiple_nested_levels():
    """Test flattening array with multiple nesting levels"""
    assert flatten_array([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]

def test_unsupported_type_raises_error():
    """Test that unsupported types raise a TypeError"""
    with pytest.raises(TypeError):
        flatten_array([1, 2, "string"])
    
    with pytest.raises(TypeError):
        flatten_array([1, [2, 3.14], 4])