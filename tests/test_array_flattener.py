import pytest
from src.array_flattener import flatten_array

def test_flatten_simple_nested_array():
    """Test flattening a simple nested array."""
    input_arr = [1, [2, 3], 4]
    assert flatten_array(input_arr) == [1, 2, 3, 4]

def test_flatten_deeply_nested_array():
    """Test flattening a deeply nested array."""
    input_arr = [1, [2, [3, 4]], 5]
    assert flatten_array(input_arr) == [1, 2, 3, 4, 5]

def test_flatten_empty_array():
    """Test flattening an empty array."""
    input_arr = []
    assert flatten_array(input_arr) == []

def test_flatten_array_with_multiple_levels():
    """Test flattening an array with multiple nested levels."""
    input_arr = [1, [2, [3, [4, 5]]], 6]
    assert flatten_array(input_arr) == [1, 2, 3, 4, 5, 6]

def test_flatten_array_with_non_list_nested_elements():
    """Test flattening an array with non-list nested elements."""
    input_arr = [1, [2, 3, [4, 'a']], 5]
    assert flatten_array(input_arr) == [1, 2, 3, 4, 'a', 5]

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_array("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_array(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_array(None)