import pytest
from um import count

def test_count():
    assert count("um") == 1
    assert count("Um, as sum that I like, um, gum") == 2
    assert count("Umm, umm, um , yum, um!") == 2


