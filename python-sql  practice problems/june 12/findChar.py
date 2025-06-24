"""Write a function in Python that accepts two string parameters. The first parameter will be a string of characters, and the second parameter will be the same string of characters, but they’ll be in a different order and have one extra character. The function should return that extra character.
For example, if the first parameter is “eueiieo” and the second is “iieoedue,” then the function should return “d.”"""

from collections import Counter

def find_char(s1, s2):
    count_s1 = Counter(s1)
    count_s2 = Counter(s2)
    for char in count_s2:
        if count_s2[char] != count_s1.get(char, 0):
            return char
    return None
s1 = input()
s2 = input()
find_char(s1, s2)
