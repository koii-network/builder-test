# Factorial Calculator

This module provides a function to calculate the factorial of a non-negative integer.

## Function Description

The `factorial(n)` function:
- Calculates the factorial of a given non-negative integer
- Uses recursive implementation
- Handles base cases (0 and 1)
- Raises a `ValueError` for negative inputs

### Example Usage

```python
from factorial import factorial

print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
```

### Error Handling

Attempting to calculate factorial of a negative number will raise a `ValueError`.