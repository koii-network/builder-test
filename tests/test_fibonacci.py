import pytest
from src.fibonacci import fibonacci_nth_term

def test_fibonacci_basic_terms():
    """Test basic Fibonacci sequence terms."""
    assert fibonacci_nth_term(0) == 0
    assert fibonacci_nth_term(1) == 1
    assert fibonacci_nth_term(2) == 1
    assert fibonacci_nth_term(3) == 2
    assert fibonacci_nth_term(4) == 3
    assert fibonacci_nth_term(5) == 5
    assert fibonacci_nth_term(6) == 8

def test_fibonacci_larger_terms():
    """Test larger Fibonacci sequence terms."""
    assert fibonacci_nth_term(10) == 55
    assert fibonacci_nth_term(15) == 610

def test_fibonacci_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="n must be a non-negative integer"):
        fibonacci_nth_term(-1)

def test_fibonacci_type_input():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError):
        fibonacci_nth_term(3.14)
    with pytest.raises(TypeError):
        fibonacci_nth_term("5")