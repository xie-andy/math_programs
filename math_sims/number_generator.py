import random

# given a mean, median, range and n, generate a random distribution of numbers

mean = 15
median = 12
low = 0
high = 30
n = 20

def num_generator(mean, median, low, high, n) -> list[int]:

    dist = []

    # idea is to generate a set of 3/4 numbers first (odd or even n), with the middle 1/2 being the median, and the other 2 smaller and bigger to achieve the mean
    # from there, just generate pairs around the median which maintain the mean property

    # first set generation

    dist.append(median)
    sum = median
    first_sum = 3*mean - median

    if (n % 2 == 0):
        dist.append(median)
        sum += median
        first_sum += mean
        first_sum -= median
    
    # next, calculate a pair

    pair_found = False

    while (not pair_found):
        x = random.randint(low, median)
        y = first_sum - x
        if (y >= median and y <= high):
            pair_found = True
            dist.append(x)
            dist.append(y)
            sum += x
            sum += y

    # next, fill in all the remaining numbers

    second_sum = 2 * mean

    while (len(dist) < n):
        x = random.randint(low, median)
        y = second_sum - x
        if (y >= median and y <= high):
            pair_found = True
            dist.append(x)
            dist.append(y)
            sum += x
            sum += y
    
    

    dist.sort()

    set_median = dist[round(n/2)]
    set_mean = sum/n

    print(set_median) 
    print(set_mean)

    return(dist)

# are these numbers truly random? they are all paired
# 

nums = num_generator(mean, median, low, high, n)
print(nums)

random.shuffle(nums)

print(nums)