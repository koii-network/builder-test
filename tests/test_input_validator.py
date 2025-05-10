"""
Comprehensive test suite for input_validator module.

Tests cover various scenarios of input validation, 
including type checking, length validation, and pattern matching.
"""

import pytest
import sys
import os

# Add src directory to path for importing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.input_validator import validate_input

def test_valid_string_input():
    """Test valid string input"""
    assert validate_input("hello", str, min_length=3, max_length=10) == "hello"

def test_valid_list_input():
    """Test valid list input"""
    assert validate_input([1, 2, 3], list, min_length=1, max_length=5) == [1, 2, 3]

def test_invalid_type():
    """Test type mismatch raises TypeError"""
    with pytest.raises(TypeError):
        validate_input(123, str)

def test_min_length_violation():
    """Test minimum length validation"""
    with pytest.raises(ValueError):
        validate_input("hi", str, min_length=3)

def test_max_length_violation():
    """Test maximum length validation"""
    with pytest.raises(ValueError):
        validate_input("toolongstring", str, max_length=5)

def test_none_input():
    """Test None input handling"""
    with pytest.raises(ValueError):
        validate_input(None, str)

def test_allow_none():
    """Test allowing None input"""
    assert validate_input(None, str, allow_empty=True) is None

def test_empty_string_not_allowed():
    """Test empty string not allowed by default"""
    with pytest.raises(ValueError):
        validate_input("", str)

def test_empty_string_allowed():
    """Test empty string when explicitly allowed"""
    assert validate_input("", str, allow_empty=True) == ""

def test_regex_validation():
    """Test regex pattern validation"""
    # Only allow lowercase letters
    assert validate_input("hello", str, regex_pattern=r'^[a-z]+$') == "hello"
    with pytest.raises(ValueError):
        validate_input("Hello123", str, regex_pattern=r'^[a-z]+$')