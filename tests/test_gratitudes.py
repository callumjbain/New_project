from lib.gratitudes import *

def test_adds_gratitude_to_list():
    new_gratitude = Gratitudes()
    new_gratitude.add("food")
    assert new_gratitude.gratitudes == ["food"]

def test_adds_items_to_list():
    gratitude = Gratitudes()
    gratitude.add("sunshine")
    gratitude.add("lollipops")
    gratitude.add("rainbows")
    result = gratitude.format()
    assert result == "Be grateful for: sunshine, lollipops, rainbows"