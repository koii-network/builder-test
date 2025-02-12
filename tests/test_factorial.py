import unittest
import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from factorial import calculate_factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        """Test factorial of 0"""
        self.assertEqual(calculate_factorial(0), 1)
    
    def test_factorial_one(self):
        """Test factorial of 1"""
        self.assertEqual(calculate_factorial(1), 1)
    
    def test_factorial_positive_numbers(self):
        """Test factorial of various positive numbers"""
        test_cases = [
            (2, 2),
            (3, 6),
            (4, 24),
            (5, 120),
            (10, 3628800)
        ]
        for num, expected in test_cases:
            self.assertEqual(calculate_factorial(num), expected)
    
    def test_negative_input(self):
        """Test that negative inputs raise ValueError"""
        with self.assertRaises(ValueError):
            calculate_factorial(-1)
        with self.assertRaises(ValueError):
            calculate_factorial(-10)
    
    def test_non_integer_input(self):
        """Test that non-integer inputs raise TypeError"""
        with self.assertRaises(TypeError):
            calculate_factorial(3.14)
        with self.assertRaises(TypeError):
            calculate_factorial("5")
        with self.assertRaises(TypeError):
            calculate_factorial([5])

if __name__ == '__main__':
    unittest.main()