import pytest
from src.array_utils import flatten_list

def test_flatten_simple_list():
    """Test flattening a simple nested list."""
    input_list = [1, [2, 3], 4]
    assert flatten_list(input_list) == [1, 2, 3, 4]

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list."""
    input_list = [1, [2, [3, 4]], [5, [6, 7]], 8]
    assert flatten_list(input_list) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_flatten_empty_list():
    """Test flattening an empty list."""
    assert flatten_list([]) == []

def test_flatten_no_nesting():
    """Test flattening a list with no nesting."""
    input_list = [1, 2, 3, 4, 5]
    assert flatten_list(input_list) == [1, 2, 3, 4, 5]

def test_flatten_mixed_types():
    """Test flattening a list with mixed types."""
    input_list = [1, 'a', [2, 'b'], [3, [4, 'c']]]
    assert flatten_list(input_list) == [1, 'a', 2, 'b', 3, 4, 'c']

def test_flatten_nested_empty_lists():
    """Test flattening a list with nested empty lists."""
    input_list = [1, [], [2, []], 3]
    assert flatten_list(input_list) == [1, 2, 3]

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_list("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_list(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_list(None)