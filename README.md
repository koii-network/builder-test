# Factorial Function

## Overview
This project implements a recursive factorial function in Python.

## Function Description
The `factorial(n)` function calculates the factorial of a non-negative integer.

### Features
- Recursive implementation
- Handles base cases (0 and 1)
- Raises ValueError for negative inputs

## Usage
```python
from factorial import factorial

print(factorial(5))  # Outputs: 120
print(factorial(0))  # Outputs: 1
```

## Running Tests
Run the tests using Python's unittest module:
```
python -m unittest test_factorial.py
```

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(n) due to recursive calls