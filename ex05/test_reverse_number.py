def reverse_number_3(num: list) -> None:

    if num == None or num < 0:
        return None

    return str(num)[::-1]

def reverse_number_2(num: list) -> None:

    if num == None or num < 0:
        return None

    reverse = ""
    for digit in str(num):
        reverse = digit + reverse

    return reverse

def reverse_number(num: int) -> None:
    if num == None or num < 0:
        return None

    reverse = ""
    for digit in reversed(str(num)):
        reverse += digit
    return reverse


def test_reverse_number() -> None:
    assert reverse_number(12345) == "54321"
    assert reverse_number(11211) == "11211"
    assert reverse_number(1) == "1"
    assert reverse_number(-1) == None
    assert reverse_number(None) == None

    assert reverse_number_2(12345) == "54321"
    assert reverse_number_2(11211) == "11211"
    assert reverse_number_2(1) == "1"
    assert reverse_number_2(-1) == None
    assert reverse_number_2(None) == None

    assert reverse_number_3(12345) == "54321"
    assert reverse_number_3(11211) == "11211"
    assert reverse_number_3(1) == "1"
    assert reverse_number_3(-1) == None
    assert reverse_number_3(None) == None
