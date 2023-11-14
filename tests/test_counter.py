from lib.counter import *

def test_counter():
    Counter.add(10)
    result = 10
    assert result == "Counted to 10 so far."