# Square Root Calculator

This project provides a simple square root calculation function with comprehensive error handling and testing.

## Features
- Calculate square root of positive numbers
- Handles various input types
- Robust error checking

## Functions
- `calculate_square_root(number)`: Calculates the square root of a given number
  - Raises `TypeError` for non-numeric inputs
  - Raises `ValueError` for negative numbers

## Usage Example
```python
from src.square_root import calculate_square_root

# Basic usage
print(calculate_square_root(4))  # Outputs: 2.0
print(calculate_square_root(2))  # Outputs: 1.414213562373095

# Error handling
try:
    calculate_square_root(-4)  # Raises ValueError
except ValueError as e:
    print(e)
```

## Running Tests
```bash
python3 -m pytest tests/test_square_root.py
```