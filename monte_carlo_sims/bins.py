# 10 balls in 5 bins
# % change of 3 balls or more in 1 bin?

import random

sims = 100000
tally = 0

for i in range(sims):

    bins = [0,0,0,0,0]

    for i in range(10):
        bin = random.randint(1,5)-1

        bins[bin] += 1
    
    for bin in bins:
        if bin > 2:
            tally += 1
            break

print(tally/sims)