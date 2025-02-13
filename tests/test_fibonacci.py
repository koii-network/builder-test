import pytest
from src.fibonacci import fibonacci_nth_term

def test_fibonacci_base_cases():
    assert fibonacci_nth_term(0) == 0
    assert fibonacci_nth_term(1) == 1

def test_fibonacci_known_terms():
    # Test some known Fibonacci sequence terms
    assert fibonacci_nth_term(2) == 1
    assert fibonacci_nth_term(3) == 2
    assert fibonacci_nth_term(4) == 3
    assert fibonacci_nth_term(5) == 5
    assert fibonacci_nth_term(6) == 8
    assert fibonacci_nth_term(10) == 55

def test_fibonacci_negative_input():
    with pytest.raises(ValueError, match="n must be a non-negative integer"):
        fibonacci_nth_term(-1)

def test_fibonacci_large_input():
    # Test a larger input to ensure the function works for bigger n
    assert fibonacci_nth_term(20) == 6765