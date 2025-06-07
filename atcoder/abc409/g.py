import math
from fractions import Fraction
N, p = map(int, input().split(" "))

prob: float = p/100
nums = {}
nums[1] = 1

for n in range(1, N):

    for key in nums:
        nums[key] *= (1 + (1-prob)/(n))

    for i in range(2, n + 2):
        if i not in nums:
            nums[i] = 0

        nums[i] += math.comb(n-1, i-2) * prob**(i-1) * (1-prob)**(n-i+1)


for value in nums.values():

    if int(value) - value == 0:
        print(int(value))
        continue

    a, b = str(Fraction(value)).split("/")
    b_inv = pow(int(b), -1, 998244353)
    result = (int(a) * b_inv) % 998244353
    print(result)
