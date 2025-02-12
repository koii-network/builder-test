# Factorial Calculator

This module provides a function to calculate the factorial of a non-negative integer.

## Function Description

The `factorial(n)` function:
- Calculates the factorial of a given non-negative integer
- Uses recursive implementation
- Handles base cases (0 and 1)
- Raises a `ValueError` for negative inputs

### Usage Example

```python
from factorial import factorial

# Calculate factorial of 5
result = factorial(5)  # Returns 120
```

### Features
- Recursive implementation
- Input validation
- Handles edge cases (0, 1)

## Factorial Definition

The factorial of a non-negative integer n, denoted as n!, is the product of all positive integers less than or equal to n.

- 0! = 1
- 1! = 1
- n! = n * (n-1)! for n > 1