import unittest
import math
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from square_root import calculate_square_root

class TestSquareRoot(unittest.TestCase):
    def test_positive_integer(self):
        """Test square root of a positive integer"""
        self.assertAlmostEqual(calculate_square_root(16), 4)
    
    def test_positive_float(self):
        """Test square root of a positive float"""
        self.assertAlmostEqual(calculate_square_root(2.0), math.sqrt(2.0))
    
    def test_zero(self):
        """Test square root of zero"""
        self.assertEqual(calculate_square_root(0), 0)
    
    def test_negative_number(self):
        """Test that a negative number raises a ValueError"""
        with self.assertRaises(ValueError):
            calculate_square_root(-4)
    
    def test_invalid_input_type(self):
        """Test that non-numeric input raises a TypeError"""
        with self.assertRaises(TypeError):
            calculate_square_root("not a number")
        with self.assertRaises(TypeError):
            calculate_square_root([1, 2, 3])
        with self.assertRaises(TypeError):
            calculate_square_root(None)

if __name__ == '__main__':
    unittest.main()