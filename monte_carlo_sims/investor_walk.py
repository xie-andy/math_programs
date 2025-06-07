import random

sims = 10000
tally = 0

for i in range(sims):

    money = 100
    days = 0
    gameover = False

    while not gameover:

        rand = random.randint(1,10)

        if (rand <= 7):
            money = money*1.01
        else:
            money = money*0.98
        
        days +=1

        if (money < 90 or money > 120):
            tally += days
            gameover = True

print(tally/sims)