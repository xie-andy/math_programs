# deck of cards
# player 1 has 1-7
# player 2 has 8-13
# on players turn, draw a card from top of the deck
# if assigned to them, they get to draw again and tick a number off
# if not their number, hand deck to other person
# winner sees all their cards first
# probability p1 wins
# cards are replaced back into the deck

import random
def andylukaevents():
    player_1_orig=[1,2,3,4,5,6,7]
    player_2_orig=[8,9,10,11,12,13]
    player_1=[1,2,3,4,5,6,7]
    player_2=[8,9,10,11,12,13]
    turn=1
    while True:
        if turn==1:
            turn=(turn+1)%2
            while True:
                randnum=random.randint(1,13)
                if randnum in player_1_orig and randnum not in player_1:
                    continue
                if randnum in player_1:
                    player_1.remove(randnum)
                    if len(player_1)==0:
                        return 1
                    continue
                else:
                    break
        if turn==0:
            turn=(turn+1)%2
            while True:
                randnum=random.randint(1,13)
                if randnum in player_2_orig and randnum not in player_2:
                    continue
                if randnum in player_2:
                    player_2.remove(randnum)
                    if len(player_2)==0:
                        return 2
                    continue
                else:
                    break
number=0
sims = 100000
for i in range(sims):
    result= andylukaevents()
    if result==1:
            number+=1
print(number/sims)
            