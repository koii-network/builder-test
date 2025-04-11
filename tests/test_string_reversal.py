import pytest
from src.string_reversal import reverse_string

def test_reverse_string_basic():
    """Test basic string reversal."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"

def test_reverse_string_empty():
    """Test reversal of an empty string."""
    assert reverse_string("") == ""

def test_reverse_string_single_char():
    """Test reversal of a single character."""
    assert reverse_string("a") == "a"

def test_reverse_string_with_spaces():
    """Test string reversal preserves spaces."""
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_string_with_special_chars():
    """Test string reversal with special characters."""
    assert reverse_string("a!b@c#") == "#c@b!a"

def test_reverse_string_invalid_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(None)

def test_reverse_string_unicode():
    """Test reversal of Unicode strings."""
    assert reverse_string("こんにちは") == "はちにんこ"

def test_implementation_method():
    """Ensure the implementation does not use slice notation or reverse()."""
    import inspect
    import src.string_reversal
    
    # Get the source code of the function
    source_lines = inspect.getsource(src.string_reversal.reverse_string)
    source_code = ''.join(source_lines)
    
    # Check that forbidden methods are not used
    assert '[::-1]' not in source_code, "Do not use slice notation for reversal"
    assert '.reverse()' not in source_code, "Do not use built-in reverse() method"