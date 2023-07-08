def anagrama_check(key_1: str, key_2: str) -> None:

    if key_1 == None or key_2 == None or type(key_1) != str or type(key_2) != str:
        return None

    key_1 = key_1.lower()
    key_2 = key_2.lower()

    key_set = {}
    for letter in key_1:
        match = key_set.get(letter)
        if not match:
            key_set[letter] = 1
        else:
            key_set[letter] += 1

    for letter in key_2:
        query = key_set.get(letter)
        if not query or query < 0:
            return False
        key_set[letter] -= 1
    for item in key_set.values():
        if item:
            return False
    return True


def test_anagrama_check() -> None:
    assert anagrama_check("Hello", 123) == None
    assert anagrama_check(123, "Olhel") == None
    assert anagrama_check("Hello", None) == None
    assert anagrama_check(None, "Olhel") == None
    assert anagrama_check("Hellooo", "Hello") == False
    assert anagrama_check("Hello", "Olhel") == True
    assert anagrama_check("Listen", "Silent") == True
    assert anagrama_check("Test", "Taste") == False
