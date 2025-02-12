import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_zero_factorial(self):
        self.assertEqual(factorial(0), 1)
    
    def test_one_factorial(self):
        self.assertEqual(factorial(1), 1)
    
    def test_positive_numbers(self):
        self.assertEqual(factorial(5), 120)  # 5! = 5 * 4 * 3 * 2 * 1
        self.assertEqual(factorial(7), 7 * 6 * 5 * 4 * 3 * 2 * 1)
    
    def test_negative_input(self):
        with self.assertRaises(ValueError):
            factorial(-1)

if __name__ == '__main__':
    unittest.main()