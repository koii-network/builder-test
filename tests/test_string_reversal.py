import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from string_reversal import reverse_string

class TestStringReversal(unittest.TestCase):
    def test_normal_string_reversal(self):
        """Test reversing a normal string"""
        self.assertEqual(reverse_string("hello"), "olleh")
    
    def test_empty_string(self):
        """Test reversing an empty string"""
        self.assertEqual(reverse_string(""), "")
    
    def test_single_character(self):
        """Test reversing a single character"""
        self.assertEqual(reverse_string("a"), "a")
    
    def test_palindrome(self):
        """Test reversing a palindrome"""
        self.assertEqual(reverse_string("racecar"), "racecar")
    
    def test_string_with_spaces(self):
        """Test reversing a string with spaces"""
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
    
    def test_string_with_special_characters(self):
        """Test reversing a string with special characters"""
        self.assertEqual(reverse_string("a1b2c3!@#"), "#@!3c2b1a")
    
    def test_invalid_input_type(self):
        """Test that a TypeError is raised for non-string inputs"""
        with self.assertRaises(TypeError):
            reverse_string(12345)
        
        with self.assertRaises(TypeError):
            reverse_string(["hello"])
        
        with self.assertRaises(TypeError):
            reverse_string(None)

if __name__ == '__main__':
    unittest.main()