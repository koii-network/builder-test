import unittest
import math
from sqrt_calculator import calculate_square_root

class TestSquareRootCalculator(unittest.TestCase):
    def test_perfect_square(self):
        self.assertAlmostEqual(calculate_square_root(16), 4.0)
        self.assertAlmostEqual(calculate_square_root(25), 5.0)
    
    def test_non_perfect_square(self):
        self.assertAlmostEqual(calculate_square_root(2), math.sqrt(2))
        self.assertAlmostEqual(calculate_square_root(10), math.sqrt(10))
    
    def test_zero(self):
        self.assertEqual(calculate_square_root(0), 0)
    
    def test_negative_number(self):
        with self.assertRaises(ValueError):
            calculate_square_root(-4)

if __name__ == '__main__':
    unittest.main()