# Fibonacci Sequence Calculator

## Overview
This module provides a function to calculate the nth term in the Fibonacci sequence.

## Function Details
`fibonacci(n)`:
- Calculates the nth term in the Fibonacci sequence (0-indexed)
- Handles base cases for 0 and 1
- Raises a `ValueError` for negative inputs
- Uses an iterative approach for efficiency

## Usage Example
```python
from fibonacci import fibonacci

# Calculate specific Fibonacci terms
print(fibonacci(0))  # 0
print(fibonacci(1))  # 1
print(fibonacci(5))  # 5
print(fibonacci(10))  # 55
```

## Time Complexity
- O(n) - Linear time complexity
- O(1) space complexity