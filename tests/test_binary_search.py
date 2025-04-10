import pytest
from src.binary_search import binary_search

def test_binary_search_basic():
    """Test basic functionality of binary search"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 7) == 3
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 13) == 6

def test_binary_search_not_found():
    """Test when target is not in the list"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 4) == -1
    assert binary_search(arr, 0) == -1
    assert binary_search(arr, 14) == -1

def test_binary_search_empty_list():
    """Test binary search on an empty list"""
    assert binary_search([], 5) == -1

def test_binary_search_single_element():
    """Test binary search on a single-element list"""
    arr = [5]
    assert binary_search(arr, 5) == 0
    assert binary_search(arr, 4) == -1

def test_binary_search_type_error():
    """Test that TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        binary_search("not a list", 5)
    with pytest.raises(TypeError):
        binary_search(123, 5)

def test_binary_search_unsorted_list():
    """Test that ValueError is raised for unsorted lists"""
    with pytest.raises(ValueError):
        binary_search([5, 3, 1, 2, 4], 3)

def test_binary_search_duplicate_elements():
    """Test binary search with duplicate elements"""
    arr = [1, 2, 2, 3, 3, 3, 4, 5]
    # Returns the index of one of the duplicates (doesn't matter which)
    assert binary_search(arr, 2) in [1, 2]
    assert binary_search(arr, 3) in [3, 4, 5]