from lib.counter import *

def test_counter():
    counter = Counter()
    counter.add(10)
    assert counter.report() == "Counted to 10 so far."

