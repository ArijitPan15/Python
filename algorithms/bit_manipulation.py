"""Bit operations on nonnegative integers."""
def count_set_bits(number):
    if number < 0:
        raise ValueError("number must be nonnegative")
    count = 0
    while number:
        number &= number - 1
        count += 1
    return count

def is_power_of_two(number):
    return number > 0 and number & (number - 1) == 0
