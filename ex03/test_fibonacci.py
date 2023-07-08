def recursive_fibonacci(nth: int) -> int:

    if nth == None:
        return None

    if nth < 1:
        return 0;
    if nth == 1:
        return 1
    return recursive_fibonacci(nth - 2) + recursive_fibonacci(nth - 1)

def fibonacci(nth: int) -> None:
    value_1 = 0
    value_2 = 1

    if nth == None or nth < 0:
        return None

    if nth == 0:
        return value_1
    if nth == 1:
        return value_2
    for _ in range(2, nth + 1):
        value_2 = value_2 + value_1
        value_1 = value_2 - value_1
    return value_2


def test_fibonacci() -> None:
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(10) == 55
    assert fibonacci(15) == 610
    assert fibonacci(-1) == None
    assert fibonacci(None) == None

    assert recursive_fibonacci(0) == 0
    assert recursive_fibonacci(1) == 1
    assert recursive_fibonacci(10) == 55
    assert recursive_fibonacci(15) == 610
    assert recursive_fibonacci(-1) == 0
    assert recursive_fibonacci(None) == None
