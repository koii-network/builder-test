# Prime Number Checker

This module provides a function `is_prime()` to check if a given number is prime.

## Features
- Efficiently checks primality of a number
- Handles edge cases like 0 and 1
- Includes test cases for verification

## Usage
```python
from prime_checker import is_prime

print(is_prime(17))  # True
print(is_prime(4))   # False
```

## How it works
The function checks primality by testing divisibility up to the square root of the number, 
which is more efficient than checking all numbers up to the input.