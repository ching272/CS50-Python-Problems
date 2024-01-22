from twttr import shorten

def test_vowel():
    assert shorten("CS50") == "CS50"

def test_cap():
    assert shorten("An apple") == "n ppl"

def test_low():
    assert shorten("what's your name?") == "wht's yr nm?"

def test_num():
    assert shorten("NUM123") == "NM123"

def test_upper():
    assert shorten("APPLE") == "PPL"

def test_punc():
    assert shorten("B.l.a.C.K") == "B.l..C.K"
