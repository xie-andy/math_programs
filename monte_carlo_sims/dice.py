import random

sims = 100000
tally = 0

for i in range(sims):

    turns = 1
    gameover = False
    alice = 0
    bob = 0

    while not gameover:
        if (turns % 3 != 0):
            alice += random.randint(1,6)
        
        if (alice >= 24):
            tally += 1
            gameover = True
        bob += random.randint(1,6)

        if (bob >= 24):
            gameover = True

        turns += 1

print(tally/sims)