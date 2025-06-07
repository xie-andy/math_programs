# first person to 3 coins wins

import random

sims = 100000
tally = 0

for i in range(sims):

    p1heads = 0
    p2heads = 0
    gameover = False

    while not gameover:
        coinflip = random.randint(1,2)

        if (coinflip == 1):
            p1heads += 1
        
        if (p1heads == 3):
            tally += 1
            gameover = True
        
        coinflip = random.randint(1,2)

        if (coinflip == 1):
            p2heads += 1

        if (p2heads == 3):
            gameover = True

print(tally/sims)