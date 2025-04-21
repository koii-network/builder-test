import pytest
from src.array_flattener import flatten_array

def test_flat_list():
    """Test flattening a list that is already flat."""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_nested_list():
    """Test flattening a list with one level of nesting."""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_deeply_nested_list():
    """Test flattening a list with multiple levels of nesting."""
    assert flatten_array([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_empty_list():
    """Test flattening an empty list."""
    assert flatten_array([]) == []

def test_list_with_empty_nested_list():
    """Test flattening a list containing an empty nested list."""
    assert flatten_array([1, [], 2]) == [1, 2]

def test_multiple_empty_nested_lists():
    """Test flattening a list with multiple empty nested lists."""
    assert flatten_array([[], [1], [], [2, []]]) == [1, 2]

def test_invalid_type_raises_error():
    """Test that an error is raised for invalid input types."""
    with pytest.raises(TypeError, match="Invalid type in array"):
        flatten_array([1, "string", 3])
    
    with pytest.raises(TypeError, match="Invalid type in array"):
        flatten_array([1, [2, "nested"], 3])

def test_complex_nested_structure():
    """Test a more complex nested structure."""
    assert flatten_array([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]

def test_nested_lists_with_different_depths():
    """Test flattening lists with varying nesting depths."""
    input_list = [1, [2], [[3]], [[[4]]], 5]
    assert flatten_array(input_list) == [1, 2, 3, 4, 5]