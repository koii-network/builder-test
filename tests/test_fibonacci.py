import pytest
from src.fibonacci import fibonacci

def test_fibonacci_base_cases():
    """Test the base cases of the Fibonacci sequence."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci sequence values."""
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(10) == 55

def test_fibonacci_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test negative input
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci("5")

def test_fibonacci_large_numbers():
    """Test larger Fibonacci sequence values."""
    assert fibonacci(20) == 6765
    assert fibonacci(30) == 832040