from lib.string_builder import *

def tests_string_builder():
    input = StringBuilder()
    input.add("test")
    assert input.size() == 4
    result = input.output()
    assert result == "test"