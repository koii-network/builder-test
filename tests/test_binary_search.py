import pytest
from src.binary_search import binary_search

def test_binary_search_found():
    """Test finding an existing element in the list"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 7) == 3
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 13) == 6

def test_binary_search_not_found():
    """Test searching for elements not in the list"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 0) == -1
    assert binary_search(arr, 14) == -1
    assert binary_search(arr, 6) == -1

def test_binary_search_empty_list():
    """Test searching in an empty list"""
    assert binary_search([], 5) == -1

def test_binary_search_single_element():
    """Test searching in a list with a single element"""
    assert binary_search([5], 5) == 0
    assert binary_search([5], 6) == -1

def test_binary_search_invalid_input():
    """Test error handling for invalid inputs"""
    # Test non-list input
    with pytest.raises(TypeError, match="Input must be a list"):
        binary_search("not a list", 5)
    
    # Test unsorted list
    with pytest.raises(ValueError, match="Input list must be sorted in ascending order"):
        binary_search([5, 3, 1], 3)

def test_binary_search_duplicates():
    """Test behavior with lists containing duplicates"""
    arr = [1, 2, 2, 3, 3, 3, 4, 4, 5]
    # Note: with multiple matches, it returns the first (lowest) index
    assert binary_search(arr, 3) in [3, 4, 5]
    assert binary_search(arr, 4) in [6, 7]