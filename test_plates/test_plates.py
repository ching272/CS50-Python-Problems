import plates
from plates import is_valid

def test_first_two_letter():
    assert is_valid("CS50") == True
    assert is_valid("C5") == False
    assert is_valid("50") == False
    assert is_valid("@@") == False
    assert is_valid("AA") == True

def test_length():
    assert is_valid("M") == False
    assert is_valid("CS123456") == False
    assert is_valid("CSCSCS") == True

def test_num():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA02") == False

def test_sym():
    assert is_valid("AA.123") == False
    assert is_valid("AA A12") == False
    assert is_valid("AA!12@") == False
