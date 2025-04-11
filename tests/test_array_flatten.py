import pytest
from src.array_flatten import flatten_array

def test_flatten_simple_list():
    """Test flattening a simple list."""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_nested_list():
    """Test flattening a nested list."""
    assert flatten_array([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]

def test_flatten_empty_list():
    """Test flattening an empty list."""
    assert flatten_array([]) == []

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list."""
    assert flatten_array([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_mixed_types_list():
    """Test flattening a list with mixed types."""
    assert flatten_array([1, 'a', [2, 'b'], [3, [4, 'c']]]) == [1, 'a', 2, 'b', 3, 4, 'c']

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_array("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_array(123)

def test_nested_empty_lists():
    """Test flattening a list with nested empty lists."""
    assert flatten_array([1, [], [2, []], 3]) == [1, 2, 3]

def test_single_element_nested_list():
    """Test flattening a list with single-element nested lists."""
    assert flatten_array([[1], [2], [3]]) == [1, 2, 3]