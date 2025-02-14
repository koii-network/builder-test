import pytest
from src.prime_numbers import find_primes_up_to_100

def test_find_primes_up_to_100():
    """Test the find_primes_up_to_100 function."""
    primes = find_primes_up_to_100()
    
    # Check that the result is a list
    assert isinstance(primes, list), "Result should be a list"
    
    # Check the number of primes
    assert len(primes) == 25, "There should be 25 prime numbers between 1 and 100"
    
    # Verify some known prime numbers are present
    expected_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
        31, 37, 41, 43, 47, 53, 59, 61, 67, 
        71, 73, 79, 83, 89, 97
    ]
    assert primes == expected_primes, "The list of primes is incorrect"
    
    # Check that all numbers in the list are prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    for num in primes:
        assert is_prime(num), f"{num} should be prime"
    
    # Check list is sorted
    assert primes == sorted(primes), "Primes should be in ascending order"