import pytest
from seasons import time_convert, valid_date

'''def test_invalid_date():
    with pytest.raises(ValueError):
        valid_date("January 1, 1999")
    with pytest.raises(ValueError):
        valid_date("01/01/1999")
'''

def test_valid_date():
    assert time_convert("13174560") == "Thirteen million, one hundred seventy-four thousand, five hundred sixty minutes"
