import random


guess = random.randint(1, 9)
invar = 0
while invar != guess:
    invar = int(input("guess a number between 1 and 9"))