"""For the purpose of this challenge, shadow sentences are sentences where every word is the same length and order but without any of the same letters. Write a function that accepts two parameters that may or may not be shadows of each other. The function should return True if they are and False if they aren’t.
An example would be “they are round” and “fold two times,” which are shadow sentences, while “his friends” and “our company” are not because both contain an r."""
def is_shadow(sentence1, sentence2):
    words = sentence1.split()
    words1 = sentence2.split()

    if len(words) != len(words1):
        return False
    for word, word1 in zip(words, words1):
        if len(word) != len(word1):
            return False
        for ch1, ch2 in zip(word, word1):
            if ch1 == ch2:
                return False
    return True
s1 = input()
s2 = input()
is_shadow(s1, s2)
"""input's: they are round
            fold two times""
