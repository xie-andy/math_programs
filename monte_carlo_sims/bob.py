# 4 people in cirlce
# equal chance to pass left, right or end the game
# finding probability bob ends the game with the balls

# pleft = 1/3
# pright = 1/3
# pend = 1/3

import random
import time
start = time.time()
game_finished = False

class Person:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        self.hasball = False

    def setLeft(self, left):
        self.left = left
    
    def setRight(self, right):
        self.right = right
    
    def setBall(self, ball):
        # ball must be bool
        self.hasball = ball
    
    def posessesBall(self):
        # return bool
        return self.hasball

bob = Person("Bob")
left = Person("left")
right = Person("right")
opposite = Person("opposite")

bob.setLeft(left)
bob.setRight(right)
bob.setBall(False)

left.setLeft(opposite)
left.setRight(bob)
bob.setBall(False)

right.setLeft(bob)
right.setRight(opposite)
bob.setBall(False)

opposite.setLeft(right)
opposite.setRight(left)
bob.setBall(False)

ball_holder = bob

sims = 100000
bob_tally = 0

for i in range(sims):

    ball_holder.setBall(False)
    ball_holder = bob
    ball_holder.setBall(True)
    game_finished = False

    while not game_finished:
        
        randint = random.randint(1, 3)
        #print(randint)

        if (randint == 1):
            #print("1.")
            game_finished = True
            if (bob.posessesBall()):
                bob_tally += 1
        
        if (randint == 2):
            # pass to left
            #print("2.")
            ball_holder.left.setBall(True)
            ball_holder.setBall(False)
            temp = ball_holder.left
            ball_holder = temp

        if (randint == 3):
            # pass to the right
            #print("3.")
            ball_holder.right.setBall(True)
            ball_holder.setBall(False)
            temp = ball_holder.right
            ball_holder = temp

print(bob_tally/sims)
print(time.time()-start)