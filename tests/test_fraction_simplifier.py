import pytest
from src.fraction_simplifier import simplify_fraction

def test_simplify_positive_fraction():
    """Test simplification of a positive fraction."""
    assert simplify_fraction(10, 25) == (2, 5)

def test_simplify_negative_fraction():
    """Test simplification of a negative fraction."""
    assert simplify_fraction(-10, 25) == (-2, 5)
    assert simplify_fraction(10, -25) == (-2, 5)
    assert simplify_fraction(-10, -25) == (2, 5)

def test_simplify_zero_numerator():
    """Test simplification when numerator is zero."""
    assert simplify_fraction(0, 5) == (0, 1)
    assert simplify_fraction(0, -5) == (0, 1)

def test_already_simplified_fraction():
    """Test a fraction that is already in its simplest form."""
    assert simplify_fraction(3, 7) == (3, 7)

def test_large_numbers():
    """Test simplification with large numbers."""
    assert simplify_fraction(1000000, 10000000) == (1, 10)

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        simplify_fraction(1.5, 2)
    
    with pytest.raises(TypeError):
        simplify_fraction(1, 2.5)
    
    with pytest.raises(TypeError):
        simplify_fraction("10", 25)

def test_zero_denominator():
    """Test error handling for zero denominator."""
    with pytest.raises(ValueError, match="Denominator cannot be zero"):
        simplify_fraction(10, 0)