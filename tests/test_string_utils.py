import pytest
from src.string_utils import reverse_string

def test_reverse_standard_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"

def test_reverse_empty_string():
    assert reverse_string("") == ""

def test_reverse_with_special_characters():
    assert reverse_string("a1b2c3!@#") == "#@!3c2b1a"

def test_reverse_with_spaces():
    assert reverse_string("hello world") == "dlrow olleh"

def test_invalid_input_type():
    with pytest.raises(TypeError):
        reverse_string(123)
    with pytest.raises(TypeError):
        reverse_string(None)
    with pytest.raises(TypeError):
        reverse_string(["not", "a", "string"])