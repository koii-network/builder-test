import pytest
from src.fraction_simplifier import simplify_fraction

def test_simplify_positive_fraction():
    """Test simplifying a positive fraction"""
    assert simplify_fraction(4, 6) == (2, 3)

def test_simplify_negative_fraction():
    """Test simplifying a negative fraction"""
    assert simplify_fraction(-4, 6) == (-2, 3)
    assert simplify_fraction(4, -6) == (-2, 3)
    assert simplify_fraction(-4, -6) == (2, 3)

def test_zero_numerator():
    """Test fraction with zero numerator"""
    assert simplify_fraction(0, 5) == (0, 1)
    assert simplify_fraction(0, -5) == (0, 1)

def test_already_simplified_fraction():
    """Test a fraction that is already in its simplest form"""
    assert simplify_fraction(5, 7) == (5, 7)

def test_large_fraction():
    """Test simplifying a larger fraction"""
    assert simplify_fraction(48, 180) == (4, 15)

def test_zero_denominator():
    """Test that zero denominator raises a ValueError"""
    with pytest.raises(ValueError, match="Denominator cannot be zero"):
        simplify_fraction(1, 0)

def test_invalid_input_types():
    """Test that non-integer inputs raise a TypeError"""
    with pytest.raises(TypeError, match="Numerator and denominator must be integers"):
        simplify_fraction(1.5, 2)
    with pytest.raises(TypeError, match="Numerator and denominator must be integers"):
        simplify_fraction(1, "2")
    with pytest.raises(TypeError, match="Numerator and denominator must be integers"):
        simplify_fraction("1", 2)