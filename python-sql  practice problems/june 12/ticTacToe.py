"""In this Python challenge, write a function that’ll accept
two numbers. These numbers will represent a position on a tic-tac-toe board.
They can be 0 through 8,where 0 is the top-left spot, and 8 is the bottom-right spot.
These parameters are two marks on the tic-tac-toe board.
The function should return the number of the spot that can block these
two spots from winning the game."""

def blocking_spot(pos1, pos2):
    winning_lines = [
        [0, 1, 2],  
        [3, 4, 5],  
        [6, 7, 8], 
        [0, 3, 6], 
        [1, 4, 7], 
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for line in winning_lines:
        if pos1 in line and pos2 in line:
            for spot in line:
                if spot != pos1 and spot != pos2:
                    return spot
    return None
