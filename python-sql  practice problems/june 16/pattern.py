"""Question
You are given an integer, N. Your task is to print an alphabet rangoli of
size N. (Rangoli is a form of Indian folk art based on creation of patterns.)
Different sizes of alphabet rangoli are shown below:
#size 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
#size 5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
Hints
First print the half of the Rangoli in the given way and save each line in a
list. Then print the list in reverse order to get the rest."""

import string
def print_pattern(n):
    alphabet = string.ascii_lowercase
    lines = []
    for i in range(n):
        line = '-'.join(alphabet[n-1:n-i-1:-1] + alphabet[n-i-1:n])
        lines.append(line.center(4*n - 3, '-'))
    print('\n'.join(lines + lines[-2::-1]))
if __name__ == "__main__":
    N = int(input())
    print_pattern(N)
