from balanced_brackets import is_balanced
def test_brackets():
    assert is_balanced("f(a[0], {x: 2})")
    assert is_balanced("")
    assert not is_balanced("([)]")
    assert not is_balanced("(")
test_brackets()
