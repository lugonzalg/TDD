import pytest

#Iterate over the string, each time a new character ir found start a counter.
#Each time, except for the first time, a character changes, fill it with the character
#followed by it number

INPUT = ["aabcccccaaa", "abcde", "aabbccddeeefffffff", "a", "aa", "aaaabbbbcccccccc", "zzzxyzzzzz", "a"*1000, ""]

RESULT = ["a2b1c5a3", "abcde", "a2b2c2d2e3f7", "a", "aa", "a4b4c8", "z3x1y1z5", "a1000", ""]

def compressor_3(in_str) -> str:

    holder = in_str[0]
    counter = 0
    out_str = ""
    for char in in_str:
        if char != holder:

            out_str += holder + str(counter)
            holder = char
            counter = 0
        counter += 1
    
    out_str += holder + str(counter)
    return out_str

def compressor_1(in_str) -> str:

    if in_str == None or type(in_str) != str:
        return None 

    holder = in_str[0]
    counter = 0
    max_repeat = 0
    max_change = 0
    out_str = ""
    for char in in_str:
        if char != holder:
            max_change += 1
            if max_repeat < counter:
                max_repeat = counter

            out_str += holder + str(counter)
            holder = char
            counter = 0
        counter += 1
    
    if max_repeat == 1 or (max_change == 0 and counter < 3):
        return in_str
    out_str += holder + str(counter)
    return out_str

def compressor_2(in_str) -> str:

    if in_str == None or type(in_str) != str:
        return None 

    in_len = len(in_str)
    if in_len == 0:
        return in_str

    holder = in_str[0]
    counter = 0
    out_str = ""
    for char in in_str:
        if char != holder:
            out_str += holder + str(counter)
            holder = char
            counter = 0
        counter += 1
    
    out_str += holder + str(counter)
    if len(in_str) <= len(out_str):
        return in_str
    return out_str


def test_compressor():
    assert compressor_1(None) == None
    assert compressor_1(123) == None
    assert compressor_2(None) == None
    assert compressor_2(123) == None
    for i in range(1, 10000000):
        for input, result in zip(INPUT, RESULT):
            assert compressor_1(input) == result
    for i in range(1, 10000000):
        for input, result in zip(INPUT, RESULT):
            assert compressor_2(input) == result

import timeit

def time_complexity_1():
    compressor_1("a"*1000)

def time_complexity_2():
    compressor_2("a"*1000)

def time_complexity_3():
    compressor_3("a"*1000)

print(timeit.timeit(time_complexity_1, number=10000))
print(timeit.timeit(time_complexity_2, number=10000))
print(timeit.timeit(time_complexity_3, number=10000))