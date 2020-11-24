import pytest

def func(x):

    return x + 1

def test_one():
    assert func(2) == 3
    #assert func(2) == 4


test_one()



