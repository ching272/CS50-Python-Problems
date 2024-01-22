import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(4)
    assert jar.capacity == 4


def test_size():
    jar = Jar()
    jar.deposit(2)
    assert str(jar) == "🍪🍪"
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    jar.withdraw(4)
    assert str(jar) == "🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(7)
    assert jar.size == 12

def test_withdraw():
    jar = Jar()
    jar.deposit(7)
    jar.withdraw(5)
    assert jar.size == 2
