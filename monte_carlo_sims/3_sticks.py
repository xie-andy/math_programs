#link: https://openquant.co/questions/three-sticks

import random

sims = 100000

tally = 0

for i in range(sims):
    stick1 = random.random()
    stick2 = random.random()

    if (stick1 > stick2):
        temp = stick1
        stick1 = stick2
        stick2 = temp
    
    # strictly increasing

    if (stick1 < 0.2):
        tally += 1
        continue
    if (stick2 - stick1 < 0.2):
        tally += 1
        continue
    if (1-stick2 < 0.2):
        tally += 1
        continue

print (tally/sims)