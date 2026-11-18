"""Integer greatest common divisor and least common multiple."""
from math import gcd

def gcd_many(*values):
    result = 0
    for value in values:
        result = gcd(result, value)
    return result

def lcm(a, b):
    return 0 if a == 0 or b == 0 else abs(a // gcd(a, b) * b)

def lcm_many(*values):
    result = 1
    for value in values:
        result = lcm(result, value)
    return result
