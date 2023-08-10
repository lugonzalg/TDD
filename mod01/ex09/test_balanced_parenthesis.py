def balanced_parenthesis(key: str) -> bool:

    if key == None or type(key) != str:
        return None

    stack = []
    opener = "("
    closer = ")"
    open_close_book = {
        "(" : ")"
    }
    for elem in key:
        if elem in opener:
            stack.append(elem)
        else:
            if len(stack) == 0:
                return False
            match = stack.pop()
            if elem != open_close_book[match]:
                return False
    if len(stack):
        return False
    return True

def test_balanced_parenthesis() -> None:
    assert balanced_parenthesis("(())") == True
    assert balanced_parenthesis("((()") == False
    assert balanced_parenthesis("(()") == False
    assert balanced_parenthesis("((()") == False
    assert balanced_parenthesis("()))") == False
