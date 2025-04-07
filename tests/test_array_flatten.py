import pytest
from src.array_flatten import flatten_array

def test_flatten_basic_nested_array():
    """Test flattening a basic nested array."""
    assert flatten_array([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]

def test_flatten_empty_array():
    """Test flattening an empty array."""
    assert flatten_array([]) == []

def test_flatten_single_level_array():
    """Test flattening an already flat array."""
    assert flatten_array([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_flatten_deeply_nested_array():
    """Test flattening a deeply nested array."""
    assert flatten_array([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_mixed_nesting():
    """Test flattening an array with mixed nesting levels."""
    assert flatten_array([1, [2, 3, [4, 5]], 6, [7, [8, 9]]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_array("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_array(123)

def test_nested_empty_arrays():
    """Test flattening nested empty arrays."""
    assert flatten_array([[], [[], []]]) == []