import pytest
from programs import Grade

def test1():
    assert Grade.calculator(25,50,100)==100

def test2():
    assert Grade.grade(80) == 'A'    

def test3():
    assert Grade.grade(61) == 'B'   

def test4():
    assert Grade.grade(56) == 'C'   

def test5():
    assert Grade.grade(46) == 'D'   

def test6():
    assert Grade.grade(12) == 'F'   