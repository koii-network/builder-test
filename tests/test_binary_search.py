import pytest
from src.binary_search import binary_search

def test_binary_search_found():
    """Test finding an existing element in the list"""
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 1) == 0
    assert binary_search([1, 2, 3, 4, 5], 5) == 4

def test_binary_search_not_found():
    """Test searching for a non-existent element"""
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    assert binary_search([1, 2, 3, 4, 5], 0) == -1

def test_binary_search_empty_list():
    """Test searching in an empty list"""
    assert binary_search([], 5) == -1

def test_binary_search_single_element():
    """Test searching in a single-element list"""
    assert binary_search([1], 1) == 0
    assert binary_search([1], 2) == -1

def test_binary_search_unsorted_list():
    """Test that an unsorted list raises a ValueError"""
    with pytest.raises(ValueError):
        binary_search([5, 2, 1, 4, 3], 3)

def test_binary_search_invalid_input():
    """Test that non-list inputs raise a TypeError"""
    with pytest.raises(TypeError):
        binary_search("not a list", 3)
    with pytest.raises(TypeError):
        binary_search(None, 3)

def test_binary_search_large_list():
    """Test binary search on a larger sorted list"""
    large_list = list(range(1000))
    assert binary_search(large_list, 500) == 500
    assert binary_search(large_list, 999) == 999
    assert binary_search(large_list, 1000) == -1