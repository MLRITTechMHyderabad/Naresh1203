"""Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?
Hints
Use for loop to iterate all possible solutions."""

heads = 35
legs = 94

for chickens in range(heads + 1):
    rabbits = heads - chickens
    if (chickens * 2) + (rabbits * 4) == legs:
        print(f"Chickens: {chickens}, Rabbits: {rabbits}")
        break
