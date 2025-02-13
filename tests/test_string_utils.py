import pytest
from src.string_utils import reverse_string

def test_reverse_string_basic():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"

def test_reverse_string_with_spaces():
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_string_with_special_chars():
    assert reverse_string("a!b@c#") == "#c@b!a"

def test_reverse_string_invalid_input():
    with pytest.raises(TypeError):
        reverse_string(123)
    with pytest.raises(TypeError):
        reverse_string(None)