import pytest
from src.fraction_simplifier import simplify_fraction

def test_simplify_standard_fraction():
    assert simplify_fraction(4, 6) == (2, 3)
    assert simplify_fraction(15, 25) == (3, 5)

def test_simplify_negative_fractions():
    assert simplify_fraction(-4, 6) == (-2, 3)
    assert simplify_fraction(4, -6) == (-2, 3)
    assert simplify_fraction(-4, -6) == (2, 3)

def test_zero_numerator():
    assert simplify_fraction(0, 5) == (0, 1)
    assert simplify_fraction(0, -5) == (0, 1)

def test_already_simplified_fraction():
    assert simplify_fraction(3, 7) == (3, 7)
    assert simplify_fraction(-3, 7) == (-3, 7)

def test_large_numbers():
    assert simplify_fraction(1000000, 10000) == (100, 1)
    assert simplify_fraction(10000, 1000000) == (1, 100)

def test_error_handling():
    # Test zero denominator
    with pytest.raises(ValueError, match="Denominator cannot be zero"):
        simplify_fraction(5, 0)

    # Test non-integer inputs
    with pytest.raises(TypeError, match="Numerator and denominator must be integers"):
        simplify_fraction(5.5, 6)
    
    with pytest.raises(TypeError, match="Numerator and denominator must be integers"):
        simplify_fraction(5, "6")
    with pytest.raises(TypeError, match="Numerator and denominator must be integers"):
        simplify_fraction("5", 6)