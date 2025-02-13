import pytest
from src.fibonacci import fibonacci_nth_term

def test_fibonacci_base_cases():
    """Test the base cases of the Fibonacci sequence."""
    assert fibonacci_nth_term(0) == 0
    assert fibonacci_nth_term(1) == 1

def test_fibonacci_known_terms():
    """Test some known Fibonacci terms."""
    assert fibonacci_nth_term(2) == 1
    assert fibonacci_nth_term(3) == 2
    assert fibonacci_nth_term(4) == 3
    assert fibonacci_nth_term(5) == 5
    assert fibonacci_nth_term(6) == 8
    assert fibonacci_nth_term(10) == 55

def test_fibonacci_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError):
        fibonacci_nth_term(-1)
    
    with pytest.raises(TypeError):
        fibonacci_nth_term("not an integer")
    
    with pytest.raises(TypeError):
        fibonacci_nth_term(3.14)