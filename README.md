# builder-test

## Square Root Calculator

This project includes a Python implementation of a square root calculation function using Newton's method.

### Features
- Calculates square root of non-negative numbers
- Uses Newton's method for approximation
- Handles edge cases like 0 and very small numbers
- Includes unit tests for verification

### Usage
```python
from sqrt import calculate_square_root

# Calculate square root
result = calculate_square_root(16)  # Returns 4.0
```

### Running Tests
To run the tests, use:
```
python -m unittest test_sqrt.py
```