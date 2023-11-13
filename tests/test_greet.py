from lib.greet import *

def tests_geet_a_person():
    result = greet('James')
    assert result == "Hello, James!"