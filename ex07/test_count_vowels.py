def count_vowels(key: str) -> int:

    if key == None or type(key) != str:
        return None

    total = 0
    for letter in key:
        if letter in "aeiou":
            total += 1
    return total

def test_count_vowels() -> None:
    assert count_vowels(1) == None
    assert count_vowels(None) == None
    assert count_vowels("qwre") == 1
    assert count_vowels("eeeeaqwre") == 6
