import pytest
from src.input_validator import validate_user_input, InputValidationError

def test_validate_input_basic_success():
    """Test basic successful input validation."""
    assert validate_user_input("hello") == "hello"
    assert validate_user_input(42) == 42
    assert validate_user_input([1, 2, 3]) == [1, 2, 3]

def test_validate_input_type_check():
    """Test type validation."""
    validate_user_input("hello", required_type=str)
    validate_user_input(42, required_type=int)
    
    with pytest.raises(InputValidationError):
        validate_user_input("hello", required_type=int)
    with pytest.raises(InputValidationError):
        validate_user_input(42, required_type=str)

def test_validate_input_length():
    """Test input length validation."""
    # Successful length validations
    validate_user_input("hello", min_length=3, max_length=5)
    validate_user_input([1, 2, 3], min_length=1, max_length=3)
    
    # Length too short
    with pytest.raises(InputValidationError):
        validate_user_input("hi", min_length=3)
    
    # Length too long
    with pytest.raises(InputValidationError):
        validate_user_input("hello world", max_length=5)

def test_validate_input_allowed_values():
    """Test allowed values validation."""
    validate_user_input("red", allowed_values=["red", "blue", "green"])
    validate_user_input(42, allowed_values=[42, 100, 200])
    
    with pytest.raises(InputValidationError):
        validate_user_input("yellow", allowed_values=["red", "blue", "green"])

def test_validate_input_none():
    """Test None input handling."""
    with pytest.raises(InputValidationError):
        validate_user_input(None)

def test_validate_input_multiple_constraints():
    """Test multiple validation constraints."""
    validate_user_input(
        "valid", 
        required_type=str, 
        min_length=3, 
        max_length=5, 
        allowed_values=["valid"]
    )
    
    with pytest.raises(InputValidationError):
        validate_user_input(
            "invalid", 
            required_type=str, 
            min_length=3, 
            max_length=5, 
            allowed_values=["valid"]
        )