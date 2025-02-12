import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)
    
    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(-5)
    
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            factorial("5")
        with self.assertRaises(TypeError):
            factorial(3.14)
        with self.assertRaises(TypeError):
            factorial(None)

if __name__ == '__main__':
    unittest.main()