from gcd_lcm import gcd_many, lcm, lcm_many
def test_number_theory():
    assert gcd_many(12, 18, 30) == 6
    assert gcd_many() == 0
    assert lcm(-6, 8) == 24
    assert lcm(0, 8) == 0
    assert lcm_many(3, 4, 6) == 12
test_number_theory()
