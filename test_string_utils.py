import unittest
from string_utils import reverse_string

class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        # Test normal string
        self.assertEqual(reverse_string("hello"), "olleh")
        
        # Test empty string
        self.assertEqual(reverse_string(""), "")
        
        # Test single character
        self.assertEqual(reverse_string("a"), "a")
        
        # Test string with spaces
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

if __name__ == '__main__':
    unittest.main()