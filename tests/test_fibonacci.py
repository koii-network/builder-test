import pytest
from src.fibonacci import fibonacci_nth_term

def test_fibonacci_basic_cases():
    # Test base cases and first few known terms
    assert fibonacci_nth_term(0) == 0
    assert fibonacci_nth_term(1) == 1
    assert fibonacci_nth_term(2) == 1
    assert fibonacci_nth_term(3) == 2
    assert fibonacci_nth_term(4) == 3
    assert fibonacci_nth_term(5) == 5
    assert fibonacci_nth_term(6) == 8

def test_fibonacci_larger_terms():
    # Test some larger terms to verify correctness
    assert fibonacci_nth_term(10) == 55
    assert fibonacci_nth_term(20) == 6765

def test_fibonacci_error_handling():
    # Test error handling for invalid inputs
    with pytest.raises(ValueError):
        fibonacci_nth_term(-1)
    
    with pytest.raises(TypeError):
        fibonacci_nth_term("not an integer")
    
    with pytest.raises(TypeError):
        fibonacci_nth_term(3.14)

def test_fibonacci_sequence_property():
    # Verify the fundamental property of Fibonacci sequence
    # Each term is the sum of the two preceding ones
    for n in range(2, 10):
        assert fibonacci_nth_term(n) == fibonacci_nth_term(n-1) + fibonacci_nth_term(n-2)