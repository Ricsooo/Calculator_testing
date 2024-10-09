import pytest
from BugtestCalc import add, substract, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(5,5) == 10
    assert add(-1,1) == 0
    assert add(-1,-1) == -2
    assert add(0,0) == 0

def test_substract():
    assert substract(10,5) == 5
    assert substract(3,10) == -7
    assert substract(5,5) == 0
    assert substract(-10,4) == -14
    assert substract(-3,-4) == 1
    assert substract(0,0) == 0

def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(5,5) == 25
    assert multiply(-1,1) == -1
    assert multiply(-1,-1) == 1
    assert multiply(0,0) == 0
    
def test_divide():
    assert divide(2, 2) == 1
    assert divide(5,5) == 1
    assert divide(31,1) == 31
    assert divide(-1,-1) == 1
