# Fibonacci Sequence Calculator

## Overview
This module provides a function to calculate the nth term in the Fibonacci sequence.

## Function: `fibonacci(n)`

### Description
Calculates the nth term in the Fibonacci sequence using an efficient iterative approach.

### Parameters
- `n` (int): The position of the term to calculate (0-indexed)

### Returns
- The nth Fibonacci number

### Example Usage
```python
print(fibonacci(0))  # Returns 0
print(fibonacci(1))  # Returns 1
print(fibonacci(5))  # Returns 5
print(fibonacci(10)) # Returns 55
```

### Notes
- Supports non-negative integers
- Raises `ValueError` for negative inputs
- 0-indexed (fibonacci(0) = 0, fibonacci(1) = 1, fibonacci(2) = 1, etc.)