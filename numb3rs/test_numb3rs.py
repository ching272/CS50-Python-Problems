import numb3rs
from numb3rs import validate

#non number input
def test_non_num():
    assert validate("cat") == False
    assert validate("cat.123.dog.321") == False

#outrange number input
def test_out_range_num():
    assert validate("0.12.2.256") == False
    assert validate("999.999.999.999") == False

#over 3 digit number input
def test_over_digit_num():
    assert validate("0.12.345.6789") == False
    assert validate("0000.0000.0000.0000") == False

#valid number input
def test_valid_num():
    assert validate("255.255.255.255") == True
    assert validate("0.1.255.23") == True
