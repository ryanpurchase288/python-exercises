import pytest
from programs import decorator_exm

def test1():
    assert decorator_exm.hello('hello') == 'HELLO'

