"""Canonical Roman numeral formatting for integers 1 through 3999."""
VALUES = ((1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I"))

def to_roman(number):
    if not isinstance(number, int) or isinstance(number, bool) or not 1 <= number <= 3999:
        raise ValueError("number must be an integer from 1 to 3999")
    result = []
    for value, numeral in VALUES:
        count, number = divmod(number, value)
        result.append(numeral * count)
    return "".join(result)
