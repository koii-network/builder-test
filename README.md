# Fibonacci Sequence Calculator

## Function Description

The `fibonacci(n)` function calculates the nth term in the Fibonacci sequence using an efficient iterative approach.

### Features
- Supports 0-indexed Fibonacci sequence calculation
- Handles base cases (0 and 1)
- Uses dynamic programming for efficient computation
- Raises a `ValueError` for negative inputs

### Usage Example
```python
from fibonacci import fibonacci

# Calculate 5th Fibonacci number (0-indexed)
result = fibonacci(5)  # Returns 5
```

### Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

### Test Cases
- fibonacci(0) returns 0
- fibonacci(1) returns 1
- fibonacci(2) returns 1
- fibonacci(5) returns 5
- fibonacci(10) returns 55