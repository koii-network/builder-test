# builder-test

## Prime Number Checker

The `prime_checker.py` module provides a function `is_prime(n)` to check if a given number is prime.

### Function Details
- Input: An integer `n`
- Output: Boolean value 
  - `True` if the number is prime
  - `False` if the number is not prime

### Usage Example
```python
from prime_checker import is_prime

print(is_prime(7))   # True
print(is_prime(10))  # False
```

### Prime Number Checking Algorithm
- Handles edge cases for numbers <= 1
- Checks divisibility up to the square root of the number
- Time complexity: O(√n)