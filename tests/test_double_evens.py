import pytest
from src.double_evens import double_even_numbers

def test_double_even_numbers_basic():
    """Test basic functionality of doubling even numbers"""
    input_list = [1, 2, 3, 4, 5, 6]
    expected = [1, 4, 3, 8, 5, 12]
    assert double_even_numbers(input_list) == expected

def test_double_even_numbers_empty_list():
    """Test with an empty list"""
    assert double_even_numbers([]) == []

def test_double_even_numbers_no_evens():
    """Test with a list containing only odd numbers"""
    input_list = [1, 3, 5, 7]
    assert double_even_numbers(input_list) == input_list

def test_double_even_numbers_all_even():
    """Test with a list containing only even numbers"""
    input_list = [2, 4, 6, 8]
    expected = [4, 8, 12, 16]
    assert double_even_numbers(input_list) == expected

def test_double_even_numbers_with_zeros():
    """Test with zero in the list"""
    input_list = [0, 1, 2, 3]
    expected = [0, 1, 4, 3]
    assert double_even_numbers(input_list) == expected

def test_double_even_numbers_with_floats():
    """Test with floating point numbers"""
    input_list = [1.5, 2.0, 3, 4.0]
    expected = [1.5, 4.0, 3, 8.0]
    assert double_even_numbers(input_list) == expected

def test_double_even_numbers_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        double_even_numbers("not a list")

def test_double_even_numbers_invalid_element_type():
    """Test that TypeError is raised for non-numeric elements"""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        double_even_numbers([1, 2, "three", 4])