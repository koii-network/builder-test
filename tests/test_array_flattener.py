import pytest
from src.array_flattener import flatten_array

def test_flatten_simple_array():
    """Test flattening a simple array."""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_nested_array():
    """Test flattening a nested array."""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_deeply_nested_array():
    """Test flattening a deeply nested array."""
    assert flatten_array([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_empty_array():
    """Test flattening an empty array."""
    assert flatten_array([]) == []

def test_flatten_single_element_array():
    """Test flattening an array with a single element."""
    assert flatten_array([42]) == [42]

def test_flatten_multiple_levels_of_nesting():
    """Test flattening an array with multiple levels of nesting."""
    assert flatten_array([1, [2, [3, [4, 5]]], 6]) == [1, 2, 3, 4, 5, 6]

def test_unsupported_type_raises_error():
    """Test that an error is raised for unsupported types."""
    with pytest.raises(TypeError):
        flatten_array([1, 2, "3"])
    
    with pytest.raises(TypeError):
        flatten_array([1, [2, 3.14], 4])

def test_mixed_nesting_with_integers():
    """Test flattening an array with mixed nesting."""
    assert flatten_array([1, [], [2, 3], [[4]], 5]) == [1, 2, 3, 4, 5]