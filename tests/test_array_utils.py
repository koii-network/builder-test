import pytest
from src.array_utils import flatten_array

def test_flatten_simple_nested_array():
    """Test flattening a simply nested array."""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_deeply_nested_array():
    """Test flattening a deeply nested array."""
    assert flatten_array([1, [2, [3, 4]], [5, [6, 7]]]) == [1, 2, 3, 4, 5, 6, 7]

def test_flatten_empty_array():
    """Test flattening an empty array."""
    assert flatten_array([]) == []

def test_flatten_single_element():
    """Test flattening a single non-list element."""
    assert flatten_array(5) == [5]

def test_flatten_mixed_types_array():
    """Test flattening an array with mixed types and nesting."""
    assert flatten_array([1, 'a', [2, [3.14]], [True, []]]) == [1, 'a', 2, 3.14, True]

def test_flatten_nested_empty_arrays():
    """Test flattening an array with nested empty arrays."""
    assert flatten_array([1, [], [2, []], 3]) == [1, 2, 3]

def test_flatten_multiple_level_nesting():
    """Test flattening an array with multiple levels of nesting."""
    nested_array = [1, [2, [3, [4, [5]]]], 6]
    assert flatten_array(nested_array) == [1, 2, 3, 4, 5, 6]