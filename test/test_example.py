from src.my_math import add_numbers, subtract_numbers, multiply_numbers

def test_add_numbers():
    assert add_numbers(5, 8) == 13

def test_subtract_numbers():
    assert subtract_numbers(8,5) == 3

def test_multiply_numbers():
    assert multiply_numbers(5,8) == 40
