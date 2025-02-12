import pytest
from src.string_reversal import reverse_string

def test_reverse_normal_string():
    assert reverse_string("hello") == "olleh"

def test_reverse_palindrome():
    assert reverse_string("racecar") == "racecar"

def test_reverse_empty_string():
    assert reverse_string("") == ""

def test_reverse_with_spaces():
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_with_special_characters():
    assert reverse_string("a1b2c3") == "3c2b1a"

def test_invalid_input_type():
    with pytest.raises(TypeError):
        reverse_string(12345)

def test_with_unicode_characters():
    assert reverse_string("こんにちは") == "はちにんこ"