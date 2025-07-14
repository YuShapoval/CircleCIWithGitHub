# test_functions.py
import pytest
from main import *

def test_is_odd():
    assert is_odd(3) is True
    assert is_odd(10) is False


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""


def test_is_palindrome():
    assert is_palindrome("level") is True
    assert is_palindrome("world") is False


def test_max_of_list():
    assert max_of_list([1, 2, 3]) == 3
    assert max_of_list([-1, -5, -3]) == -1
    with pytest.raises(ValueError):
        max_of_list([])