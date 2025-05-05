import pytest
from src.array_flattener import flatten_array

def test_flatten_simple_nested_list():
    input_list = [1, [2, 3], 4]
    assert flatten_array(input_list) == [1, 2, 3, 4]

def test_flatten_deeply_nested_list():
    input_list = [1, [2, [3, 4]], 5]
    assert flatten_array(input_list) == [1, 2, 3, 4, 5]

def test_flatten_multiple_level_nesting():
    input_list = [1, [2, [3, [4, 5]]], 6]
    assert flatten_array(input_list) == [1, 2, 3, 4, 5, 6]

def test_flatten_empty_list():
    assert flatten_array([]) == []

def test_flatten_single_integer():
    assert flatten_array(5) == [5]

def test_invalid_element_type():
    with pytest.raises(TypeError, match="Invalid element type"):
        flatten_array([1, 2, "three"])

def test_mixed_nested_lists():
    input_list = [1, [2, 3, [4, [5]]], 6]
    assert flatten_array(input_list) == [1, 2, 3, 4, 5, 6]