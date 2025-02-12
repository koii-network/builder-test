import pytest
from src.fibonacci import calculate_fibonacci

def test_fibonacci_base_cases():
    """Test base cases for Fibonacci sequence."""
    assert calculate_fibonacci(0) == 0
    assert calculate_fibonacci(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci sequence values."""
    test_cases = [
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (10, 55)
    ]
    for n, expected in test_cases:
        assert calculate_fibonacci(n) == expected

def test_fibonacci_error_handling():
    """Test error handling for invalid inputs."""
    # Test negative input
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        calculate_fibonacci(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_fibonacci(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_fibonacci("5")

def test_fibonacci_large_n():
    """Test Fibonacci calculation for larger n values."""
    # Large n to check for performance and correctness
    assert calculate_fibonacci(20) == 6765
    assert calculate_fibonacci(30) == 832040