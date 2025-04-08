import pytest
from src.array_flattener import flatten_array

def test_basic_flattening():
    """Test basic array flattening with simple nested lists"""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_multiple_nested_levels():
    """Test flattening arrays with multiple levels of nesting"""
    assert flatten_array([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_empty_array():
    """Test flattening an empty array"""
    assert flatten_array([]) == []

def test_no_nesting():
    """Test flattening an array with no nesting"""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_deeply_nested_array():
    """Test flattening a deeply nested array"""
    assert flatten_array([1, [2, [3, [4, [5]]]], 6]) == [1, 2, 3, 4, 5, 6]

def test_mixed_nesting():
    """Test flattening an array with mixed nesting patterns"""
    assert flatten_array([1, [2], [[3]], [[[4]]], 5]) == [1, 2, 3, 4, 5]

def test_invalid_input_type():
    """Test that a non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_array(123)

def test_invalid_element_type():
    """Test that an invalid element type raises a TypeError"""
    with pytest.raises(TypeError, match="Invalid element type"):
        flatten_array([1, 2, "3"])
        
def test_nested_invalid_type():
    """Test that nested invalid types raise a TypeError"""
    with pytest.raises(TypeError, match="Invalid element type"):
        flatten_array([1, [2, "3"], 4])