import pytest
from src.fibonacci import fibonacci_nth_term

def test_fibonacci_nth_term_basic_cases():
    """Test basic Fibonacci sequence cases."""
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
    assert fibonacci_nth_term(20) == 6765

def test_fibonacci_negative_input():
    """Test that the function raises a ValueError for negative inputs."""
    with pytest.raises(ValueError, match="Position must be a non-negative integer"):
        fibonacci_nth_term(-1)
    with pytest.raises(ValueError, match="Position must be a non-negative integer"):
        fibonacci_nth_term(-10)