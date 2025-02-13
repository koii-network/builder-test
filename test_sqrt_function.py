import unittest
from sqrt_function import calculate_square_root

class TestSquareRootFunction(unittest.TestCase):
    def test_perfect_squares(self):
        """Test square roots of perfect squares"""
        test_cases = [
            (0, 0),
            (4, 2),
            (9, 3),
            (16, 4),
            (25, 5)
        ]
        for input_num, expected in test_cases:
            self.assertAlmostEqual(calculate_square_root(input_num), expected)
    
    def test_non_perfect_squares(self):
        """Test square roots of non-perfect squares"""
        test_cases = [
            (2, 1.4142),
            (10, 3.1623),
            (7, 2.6458)
        ]
        for input_num, expected in test_cases:
            self.assertAlmostEqual(calculate_square_root(input_num), expected, places=4)
    
    def test_negative_number(self):
        """Test that negative numbers raise a ValueError"""
        with self.assertRaises(ValueError):
            calculate_square_root(-1)

if __name__ == '__main__':
    unittest.main()