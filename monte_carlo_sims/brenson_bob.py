import random
import time
def testfunction():
    position=0
    while True:
        randnum=random.randint(1,3)
        if randnum==2:
            return position
        else:
            position=(position+randnum)%4
counter=0
start = time.time()
for i in range(100000):
    pos=testfunction()
    if pos==0:
        counter+=1
print(counter/100000)
print(time.time()-start)
