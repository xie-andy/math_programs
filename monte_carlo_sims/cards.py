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

p1_cards = [i for i in range(1, 8)]
p2_cards = [i for i in range(8, 14)]

sims = 10000
p1tally = 0

for i in range(sims):
    
    deck_holder = 1
    p1 = [i for i in range(1, 8)]
    p2 = [i for i in range(8, 14)]
    game_ended = False

    while (not game_ended):
        card = random.randint(1, 13)

        if (deck_holder == 1) and (card in p1_cards):
            if (card in p1):
                p1.remove(card)
            if len(p1) == 0:
                game_ended = True
                p1tally += 1

        if (deck_holder == 2) and (card in p2_cards):
            if (card in p2):
                p2.remove(card)
            if len(p2) == 0:
                game_ended = True

        if (deck_holder == 1) and (card not in p1_cards):
            deck_holder = 2
        
        if (deck_holder == 2) and (card not in p2_cards):
            deck_holder = 1

print(p1tally/sims)