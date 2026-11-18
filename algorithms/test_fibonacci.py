from fibonacci import fibonacci
def test_fibonacci():
    assert [fibonacci(n) for n in range(8)] == [0,1,1,2,3,5,8,13]
    assert fibonacci(50) == 12586269025
    try: fibonacci(-1)
    except ValueError: pass
    else: raise AssertionError("expected ValueError")
test_fibonacci()
