"""For this challenge, you need to write a function in Python that accepts
a string of ASCII characters. It should return each character’s value as a
hexadecimal string. Separate each byte by a space, and return all alpha
hexadecimal characters as lowercase"""

def string_to_hex(s):
    return ' '.join(f"{ord(char):02x}" for char in s)
s = input()
string_to_hex(s)
