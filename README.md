# String Utilities

## String Reversal Function

This module provides a utility function `reverse_string()` that efficiently reverses a given string.

### Features
- Reverses any input string
- Handles empty strings
- Works with strings containing special characters

### Usage Example
```python
from string_utils import reverse_string

print(reverse_string("hello"))  # Outputs: olleh
print(reverse_string(""))       # Outputs: 
print(reverse_string("python")) # Outputs: nohtyp
```

### Implementation
The function uses Python's slice notation `[::-1]` for an efficient string reversal.