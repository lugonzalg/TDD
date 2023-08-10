def palindrome(key: str) -> bool:

    if key == None or type(key) != str:
        return None

    key = key.replace(" ", "").lower()

    key_len = len(key) - 1
    for i, letter in enumerate(key):
        if key[i] != key[key_len - i]:
            return False
    return True

def test_palindrome() -> None:
    assert palindrome(1) == None
    assert palindrome(None) == None
    assert palindrome("r") == True
    assert palindrome("radar") == True
    assert palindrome("Hello") == False
    assert palindrome("A man a plan a canal Panama") == True
