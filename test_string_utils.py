from string_utils import reverse_string

def test_reverse_string():
    # Test standard string reversal
    assert reverse_string("hello") == "olleh"
    
    # Test empty string
    assert reverse_string("") == ""
    
    # Test palindrome
    assert reverse_string("racecar") == "racecar"
    
    # Test string with special characters
    assert reverse_string("Hello, World!") == "!dlroW ,olleH"

    print("All tests passed!")

# Run the tests
test_reverse_string()