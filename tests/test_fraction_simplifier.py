import pytest
from src.fraction_simplifier import simplify_fraction

def test_simplify_basic_fraction():
    """Test simplifying a basic fraction"""
    assert simplify_fraction(4, 6) == (2, 3)

def test_simplify_already_simplified():
    """Test a fraction that is already in its simplest form"""
    assert simplify_fraction(5, 7) == (5, 7)

def test_simplify_zero_numerator():
    """Test simplifying a fraction with zero numerator"""
    assert simplify_fraction(0, 5) == (0, 1)

def test_simplify_negative_fraction():
    """Test simplifying a fraction with negative numbers"""
    assert simplify_fraction(-4, 6) == (-2, 3)
    assert simplify_fraction(4, -6) == (-2, 3)
    assert simplify_fraction(-4, -6) == (2, 3)

def test_large_fraction():
    """Test simplifying a large fraction"""
    assert simplify_fraction(1000, 10000) == (1, 10)

def test_zero_denominator():
    """Test that zero denominator raises a ValueError"""
    with pytest.raises(ValueError, match="Denominator cannot be zero"):
        simplify_fraction(5, 0)

def test_non_integer_input():
    """Test that non-integer inputs raise a TypeError"""
    with pytest.raises(TypeError, match="Numerator and denominator must be integers"):
        simplify_fraction(5.5, 7)
    with pytest.raises(TypeError, match="Numerator and denominator must be integers"):
        simplify_fraction(5, "7")
    with pytest.raises(TypeError, match="Numerator and denominator must be integers"):
        simplify_fraction("5", 7)