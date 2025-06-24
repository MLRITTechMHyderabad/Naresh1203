"""Create a function in Python that accepts one parameter:
a string that’s a sentence. This function should return True
if any word in that sentence contains duplicate letters and False if not."""

def find_duplicates(sentence):
    for word in sentence.split():
        seen = set()
        for char in word:
            if char in seen:
                return True
            seen.add(char)
    return False
s = input()
find_duplicates(s)
