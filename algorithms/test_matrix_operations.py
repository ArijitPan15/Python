from matrix_operations import transpose, matrix_add
def test_matrix():
    assert transpose([[1,2],[3,4]]) == [[1,3],[2,4]]
    assert transpose([]) == []
    assert matrix_add([[1,2]], [[3,4]]) == [[4,6]]
    try: transpose([[1,2],[3]])
    except ValueError: pass
    else: raise AssertionError("expected ValueError")
test_matrix()
