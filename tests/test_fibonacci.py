import pytest
from src.fibonacci import fibonacci_nth_term

def test_fibonacci_base_cases():
    """Test the base cases of the Fibonacci sequence."""
    assert fibonacci_nth_term(0) == 0
    assert fibonacci_nth_term(1) == 1

def test_fibonacci_known_terms():
    """Test known Fibonacci terms."""
    # Test sequence up to 10th term
    expected_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, expected in enumerate(expected_sequence):
        assert fibonacci_nth_term(i) == expected

def test_negative_input():
    """Test that a negative input raises a ValueError."""
    with pytest.raises(ValueError, match="n must be a non-negative integer"):
        fibonacci_nth_term(-1)

def test_larger_terms():
    """Test larger Fibonacci terms."""
    # Verify some larger known Fibonacci numbers
    assert fibonacci_nth_term(10) == 55
    assert fibonacci_nth_term(15) == 610
    assert fibonacci_nth_term(20) == 6765