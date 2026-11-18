from prime_sieve import sieve
def test_sieve():
    assert sieve(1) == []
    assert sieve(2) == [2]
    assert sieve(20) == [2, 3, 5, 7, 11, 13, 17, 19]
test_sieve()
