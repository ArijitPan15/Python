from prefix_sums import prefix_sums, range_sum
def test_prefix():
    p = prefix_sums([2, -3, 5])
    assert p == [0, 2, -1, 4]
    assert range_sum(p, 1, 3) == 2
    try: range_sum(p, -1, 2)
    except IndexError: pass
    else: raise AssertionError("expected IndexError")
test_prefix()
