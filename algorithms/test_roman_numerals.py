from roman_numerals import to_roman
def test_roman():
    assert to_roman(4) == "IV"
    assert to_roman(1994) == "MCMXCIV"
    assert to_roman(3999) == "MMMCMXCIX"
    try: to_roman(0)
    except ValueError: pass
    else: raise AssertionError("expected ValueError")
test_roman()
