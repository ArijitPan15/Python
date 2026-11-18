from run_length import encode, decode
def test_rle():
    for text in ("", "a", "aaabbc", "111222", "a b"):
        assert decode(encode(text)) == text
    try: decode([("a", -1)])
    except ValueError: pass
    else: raise AssertionError("expected ValueError")
test_rle()
