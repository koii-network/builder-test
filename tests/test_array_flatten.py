import pytest
from src.array_flatten import flatten_array

def test_flatten_simple_list():
    """Test flattening a simple list with no nesting."""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_single_level_nested():
    """Test flattening a list with single-level nesting."""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_multi_level_nested():
    """Test flattening a list with multiple levels of nesting."""
    assert flatten_array([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_empty_list():
    """Test flattening an empty list."""
    assert flatten_array([]) == []

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list."""
    assert flatten_array([1, [2, [3, [4, [5]]]], 6]) == [1, 2, 3, 4, 5, 6]

def test_invalid_input_type():
    """Test that a non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_array(123)

def test_invalid_nested_type():
    """Test that an unsupported type in the list raises a TypeError."""
    with pytest.raises(TypeError, match="Unsupported type"):
        flatten_array([1, 2, "string"])

def test_mixed_nesting():
    """Test flattening a list with mixed nesting levels."""
    assert flatten_array([1, [2], [[3]], [[[4]]], 5]) == [1, 2, 3, 4, 5]