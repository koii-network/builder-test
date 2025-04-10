import pytest
from src.array_flatten import flatten_array

def test_flatten_simple_list():
    """Test flattening a simple list."""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_nested_list():
    """Test flattening a nested list."""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list."""
    assert flatten_array([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_empty_list():
    """Test flattening an empty list."""
    assert flatten_array([]) == []

def test_flatten_multiple_nested_lists():
    """Test flattening multiple nested lists."""
    assert flatten_array([[1, 2], [3, [4, 5]], 6]) == [1, 2, 3, 4, 5, 6]

def test_invalid_input_raises_error():
    """Test that non-integer and non-list inputs raise a TypeError."""
    with pytest.raises(TypeError):
        flatten_array([1, 2, "3"])
    
    with pytest.raises(TypeError):
        flatten_array([1, 2, None])

def test_flatten_single_element_list():
    """Test flattening a list with a single nested list."""
    assert flatten_array([1, [2], 3]) == [1, 2, 3]