import time
import math

def is_prime_number_gpt(num: int) -> bool:
    if not num:
        return None

    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i == 0):
            return False
    return True

def is_prime_number(num: int) -> bool:
    if not num:
        return None

    for i in range(2, num):
        if (num % i == 0):
            return False
        elif (i * i) > num:
            break
    return True

def wraper(num: int, flag: bool) -> None:

    t = time.process_time()
    assert is_prime_number(num) == flag
    elapsed = time.process_time() - t
    print(f" TRY 1 ME {elapsed}")

    t = time.process_time()
    assert is_prime_number_gpt(num) == flag
    elapsed = time.process_time() - t
    print(f" TRY 1 GPT {elapsed}")

def test_prime_number() -> None:

    wraper(2, True)
    wraper(7, True)
    wraper(123, False)
    wraper(137, True)

def get_factorial(num: int) -> int:
    if not num:
        return None

    total = 1
    for i in range(1, num + 1):
        print(total)
        total *= i
    return total

def test_factorial_number() -> None:
    num = 2
    assert get_factorial(num) == 2
    num = 7
    assert get_factorial(num) == 5_040
    num = 11
    assert get_factorial(num) == 39_916_800
    num = None
    assert get_factorial(num) == None

test_prime_number()
