# Fibonacci Sequence Calculator

## Overview
This module provides a function to calculate the nth term in the Fibonacci sequence efficiently.

## Function Description
`fibonacci(n)` calculates the nth term in the Fibonacci sequence with the following characteristics:
- Handles 0-indexed input
- Uses an iterative approach for better performance
- Raises a `ValueError` for negative inputs

## Example Usage
```python
from fibonacci import fibonacci

# Calculate specific Fibonacci terms
print(fibonacci(0))  # 0
print(fibonacci(1))  # 1
print(fibonacci(5))  # 5
print(fibonacci(10)) # 55
```

## Time Complexity
- O(n) time complexity
- O(1) space complexity

## Notes
- First term (n=0) is 0
- Second term (n=1) is 1
- Subsequent terms are the sum of the two preceding terms