import pytest
from src.lcm_calculator import lcm, lcm_multiple

def test_lcm_basic():
    assert lcm(4, 6) == 12
    assert lcm(15, 25) == 75
    assert lcm(3, 7) == 21

def test_lcm_same_number():
    assert lcm(5, 5) == 5
    assert lcm(10, 10) == 10

def test_lcm_coprime_numbers():
    assert lcm(7, 13) == 91
    assert lcm(17, 19) == 323

def test_lcm_multiple_numbers():
    assert lcm_multiple(2, 3, 4) == 12
    assert lcm_multiple(3, 4, 6) == 12
    assert lcm_multiple(2, 3, 5, 7) == 210

def test_lcm_error_handling():
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        lcm(-1, 5)
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        lcm(5, -1)
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        lcm(-3, -4)
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        lcm(0, 5)

def test_lcm_multiple_error_handling():
    with pytest.raises(ValueError, match="At least one number must be provided"):
        lcm_multiple()
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        lcm_multiple(2, 3, -4)

def test_lcm_large_numbers():
    assert lcm(1000000, 1500000) == 3000000
    assert lcm(123456, 789012) == 2222625456