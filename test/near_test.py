import pytest
from programs import near

def test_near():
   assert near.near('reset','rest')==True

def test_near_false():
   assert near.near('wrong','big')==False