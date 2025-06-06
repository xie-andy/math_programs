# problem: 2 people arrive in a park and stay for 15 minutes
# what is the probability they see each other?

import random

sims = 1000000
tally = 0

for i in range(sims):
    person1 = 60 * random.random()
    person2 = 60 * random.random()

    if (abs(person1-person2) < 15):
        tally +=1

print (tally/sims)