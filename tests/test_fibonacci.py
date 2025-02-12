import pytest
from src.fibonacci import fibonacci_nth_term

def test_fibonacci_base_cases():
    assert fibonacci_nth_term(0) == 0
    assert fibonacci_nth_term(1) == 1

def test_fibonacci_known_terms():
    assert fibonacci_nth_term(2) == 1
    assert fibonacci_nth_term(3) == 2
    assert fibonacci_nth_term(4) == 3
    assert fibonacci_nth_term(5) == 5
    assert fibonacci_nth_term(6) == 8
    assert fibonacci_nth_term(10) == 55

def test_fibonacci_error_handling():
    # Test negative input
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_nth_term(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_nth_term(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_nth_term("5")

def test_fibonacci_large_input():
    # Test a larger Fibonacci number to ensure performance
    assert fibonacci_nth_term(20) == 6765