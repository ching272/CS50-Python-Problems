from bank import value

def test_hello():
    assert value("HEllo") == 0
    assert value("Hello, Newman") == 0

def test_h():
    assert value("hey") == 20
    assert value("   How you doing?   ") == 20

def test_not_h():
    assert value("What's up?") == 100
    assert value("What's happening?") == 100



