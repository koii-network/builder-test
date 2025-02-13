import unittest
from sqrt import calculate_square_root

class TestSquareRoot(unittest.TestCase):
    def test_square_root_positive_numbers(self):
        """Test square root calculation for various positive numbers"""
        test_cases = [
            (0, 0),
            (4, 2),
            (9, 3),
            (16, 4),
            (25, 5)
        ]
        
        for input_num, expected in test_cases:
            with self.subTest(input_num=input_num):
                result = calculate_square_root(input_num)
                self.assertAlmostEqual(result, expected, places=10)
    
    def test_square_root_negative_number(self):
        """Test that a ValueError is raised for negative numbers"""
        with self.assertRaises(ValueError):
            calculate_square_root(-1)

if __name__ == '__main__':
    unittest.main()