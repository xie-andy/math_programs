# making it to work
# link: https://www.youtube.com/watch?v=slbZ-SLpIgg
# given 2 random variables, what are chances that variables sum to 9 or less?
# first random variable is 1-5, second is 2-6

import random

def random_float(offset, scale):
    seed = random.random()
    randint = (seed*scale) + offset
    return randint

n = 1000000 # replace with how many simulations
results = [0, 0]

for i in range(n):
    if (random.randint(1, 5) + random.randint(2, 6)) > 9:
        results[1] += 1
    else:
        results[0] += 1

print(results)

results = [0, 0]

for i in range(n):
    if (random_float(1, 4) + random_float(2, 4)) > 9:
        results[1] += 1
    else:
        results[0] += 1

print(results)
