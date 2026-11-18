from kadane import max_subarray_sum
def test_kadane():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert max_subarray_sum([-5,-1,-3]) == -1
    try: max_subarray_sum([])
    except ValueError: pass
    else: raise AssertionError("expected ValueError")
test_kadane()
