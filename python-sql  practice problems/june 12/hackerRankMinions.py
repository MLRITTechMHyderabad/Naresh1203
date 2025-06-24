"""https://www.hackerrank.com/challenges/the-minion-game/problem"""

def minion_game(string):
    vowels = 'AEIOU'
    kevin = 0
    stuart_score = 0
    length = len(string)

    for i in range(length):
        if string[i] in vowels:
            kevin += length - i
        else:
            stuart_score += length - i

    if kevin > stuart_score:
        print("Kevin", kevin)
    elif stuart_score > kevin:
        print("Stuart", stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
