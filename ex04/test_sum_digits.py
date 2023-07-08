def sum_digits(num: int) -> None:
    if num == None or num < 0:
        return None

    total = 0
    for digit in str(num):
        total += int(digit)
    return total

def test_sum_digits() -> None:
    assert sum_digits(123) == 6
    assert sum_digits(45678) == 30
    assert sum_digits(0) == 0
    assert sum_digits(-1) == None
    assert sum_digits(None) == None
