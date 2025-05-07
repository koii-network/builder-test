import pytest
from src.array_utils import flatten

def test_flatten_simple_list():
    """Test flattening a simple list"""
    assert flatten([1, 2, 3]) == [1, 2, 3]

def test_flatten_nested_list():
    """Test flattening a list with one level of nesting"""
    assert flatten([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_deeply_nested_list():
    """Test flattening a list with multiple levels of nesting"""
    assert flatten([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_complex_nested_list():
    """Test flattening a more complex nested list"""
    assert flatten([1, [2, [3, [4, 5]]], 6]) == [1, 2, 3, 4, 5, 6]

def test_flatten_empty_list():
    """Test flattening an empty list"""
    assert flatten([]) == []

def test_flatten_non_list_single_element():
    """Test flattening a single non-list element"""
    assert flatten(42) == [42]

def test_flatten_mixed_types():
    """Test flattening a list with mixed types of nested elements"""
    assert flatten([1, [2, 'three'], [4, [5, None]]]) == [1, 2, 'three', 4, 5, None]

def test_nested_empty_lists():
    """Test flattening lists containing empty lists"""
    assert flatten([1, [], [2, []], 3]) == [1, 2, 3]