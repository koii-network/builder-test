import pytest
from src.array_flattener import flatten_array

def test_flatten_basic():
    """Test basic flattening of a nested list"""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_multi_level():
    """Test flattening of multi-level nested lists"""
    assert flatten_array([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_empty_list():
    """Test flattening an empty list"""
    assert flatten_array([]) == []

def test_flatten_no_nesting():
    """Test flattening a list with no nesting"""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_deeply_nested():
    """Test flattening a deeply nested list"""
    assert flatten_array([1, [2, [3, [4, [5]]]], 6]) == [1, 2, 3, 4, 5, 6]

def test_flatten_mixed_nesting():
    """Test flattening a list with mixed nesting levels"""
    assert flatten_array([1, [2], [[3]], [[[4]]], 5]) == [1, 2, 3, 4, 5]

def test_invalid_type_raises_error():
    """Test that non-integer/list types raise a TypeError"""
    with pytest.raises(TypeError):
        flatten_array([1, 2, "3"])
    
    with pytest.raises(TypeError):
        flatten_array([1, [2, 3.5], 4])

def test_none_raises_error():
    """Test that None values raise a TypeError"""
    with pytest.raises(TypeError):
        flatten_array([1, None, 2])