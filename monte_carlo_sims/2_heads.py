# question: EV of number of flips before seeing 2 heads in a row

import random

sims = 1000000

flips = 0

for i in range(sims):
    head_count = 0
    total_count = 0
    while (head_count < 2):
        if (random.randint(1, 2) == 1):
            # heads
            head_count += 1
        else:
            head_count = 0
        total_count += 1

    flips += total_count

EV = flips/sims
print(EV)