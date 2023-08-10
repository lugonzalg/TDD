def get_index_n2(nums: list, result: int) -> list:
    if not nums:
        return None

    for i, num in enumerate(nums):
        for j, num in enumerate(nums):
            if i != j and nums[i] + nums[j] == result:
                return [i, j]

def get_index_n(nums: list, result: int) -> list:
    if not nums:
        return None

    nums_book = {}

    for i, num in enumerate(nums):
        sub = result - num
        if _num := nums_book.get(sub):
            return i, _num["index"]
        nums_book[num] = {"index" : i}

def test_get_index() -> None:
    nums = [2, 7, 11, 0, 9]
    bad_nums = None
    result = 11
    bad_result = 123
    assert get_index_n2(nums, result) == [0, 4]
    assert get_index_n(nums, result) == [0, 4] or [3, 2]
    assert get_index_n2(nums, bad_result) == None
    assert get_index_n(nums, bad_result) == None
    assert get_index_n2(bad_nums, result) == None
    assert get_index_n(bad_nums, result) == None
    assert get_index_n2(bad_nums, bad_result) == None
    assert get_index_n(bad_nums, bad_result) == None
