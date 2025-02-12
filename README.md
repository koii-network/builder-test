# Factorial Calculator

This module provides a function to calculate the factorial of a non-negative integer.

## Function Description

The `factorial(n)` function calculates the factorial of a given non-negative integer `n`. 

### Features
- Handles 0 and 1 as special cases
- Raises a `ValueError` for negative numbers
- Raises a `TypeError` for non-integer inputs

### Usage Example
```python
from factorial import factorial

print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
```

### Error Handling
- Negative numbers will raise a `ValueError`
- Non-integer inputs will raise a `TypeError`