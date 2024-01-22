from fuel import convert, gauge
import pytest

def test_convert_value_error():
    with pytest.raises(ValueError):
        assert convert("3/2")
    with pytest.raises(ValueError):
        assert convert("5.5/5")
    with pytest.raises(ValueError):
        assert convert("5.5/50")
    with pytest.raises(ValueError):
        assert convert("cat/dog")
    with pytest.raises(ValueError):
        assert convert("cat/5")
    with pytest.raises(ValueError):
        assert convert("5/cat")
    with pytest.raises(ValueError):
        assert convert("cat/0")

def test_convert_zero_divine():
    with pytest.raises(ZeroDivisionError):
        assert convert("5/0")
    with pytest.raises(ZeroDivisionError):
        assert convert("100/0")

def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_gauge_num():
    assert gauge(98) == "98%"
    assert gauge(2) == "2%"
    assert gauge(27) == "27%"

def test_convert_num():
    assert convert("1/4") == 25
    assert convert("1/5") == 20
    assert convert("0/100") == 0
    
