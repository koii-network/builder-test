import unittest
from factorial import calculate_factorial

class TestFactorial(unittest.TestCase):
    def test_zero_factorial(self):
        """Test factorial of 0 is 1"""
        self.assertEqual(calculate_factorial(0), 1)
    
    def test_one_factorial(self):
        """Test factorial of 1 is 1"""
        self.assertEqual(calculate_factorial(1), 1)
    
    def test_small_positive_factorial(self):
        """Test factorial of small positive numbers"""
        self.assertEqual(calculate_factorial(5), 120)  # 5! = 120
        self.assertEqual(calculate_factorial(3), 6)    # 3! = 6
    
    def test_larger_factorial(self):
        """Test factorial of larger numbers"""
        self.assertEqual(calculate_factorial(10), 3628800)
    
    def test_negative_input(self):
        """Test that negative inputs raise a ValueError"""
        with self.assertRaises(ValueError):
            calculate_factorial(-1)
    
    def test_non_integer_input(self):
        """Test that non-integer inputs raise a TypeError"""
        with self.assertRaises(TypeError):
            calculate_factorial(3.14)
        with self.assertRaises(TypeError):
            calculate_factorial("5")

if __name__ == '__main__':
    unittest.main()