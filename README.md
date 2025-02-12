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

## Running Tests
```bash
python3 -m pytest tests/test_square_root.py
```