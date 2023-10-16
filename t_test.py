from t import is_prime
import pytest


@pytest.mark.parametrize(
    'num', (
        (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
         41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    )
)
def test_is_prime_for_prime_number(num):
    assert is_prime(num) == True

def test_is_prime_for_negative_number():
    assert is_prime(-1) == False
