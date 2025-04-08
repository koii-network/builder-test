import pytest
from src.array_flattener import flatten_array

def test_flatten_simple_array():
    """Test flattening a simple array"""
    input_array = [1, 2, 3, 4, 5]
    assert flatten_array(input_array) == [1, 2, 3, 4, 5]

def test_flatten_nested_array():
    """Test flattening a nested array"""
    input_array = [1, [2, 3], [4, [5, 6]]]
    assert flatten_array(input_array) == [1, 2, 3, 4, 5, 6]

def test_flatten_deeply_nested_array():
    """Test flattening a deeply nested array"""
    input_array = [1, [2, [3, [4]]], 5]
    assert flatten_array(input_array) == [1, 2, 3, 4, 5]

def test_flatten_mixed_types():
    """Test flattening an array with mixed types"""
    input_array = [1, 'a', [2, 'b'], [3, [4, 'c']]]
    assert flatten_array(input_array) == [1, 'a', 2, 'b', 3, 4, 'c']

def test_flatten_empty_array():
    """Test flattening an empty array"""
    input_array = []
    assert flatten_array(input_array) == []

def test_flatten_array_with_empty_lists():
    """Test flattening an array containing empty lists"""
    input_array = [1, [], [2, []], 3]
    assert flatten_array(input_array) == [1, 2, 3]

def test_invalid_input():
    """Test that non-list input raises TypeError"""
    with pytest.raises(TypeError):
        flatten_array("not a list")
    with pytest.raises(TypeError):
        flatten_array(123)
    with pytest.raises(TypeError):
        flatten_array(None)