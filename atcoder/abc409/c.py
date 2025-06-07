n, l = input().split(" ")
n = int(n)
l = int(l)
d = input().split(" ")
d = list(map(int, d))

if l % 3 != 0:
    print(0)
    exit()

dict = {}
dict[0] = 1
sum = 0

for entry in d:
    sum += entry
    new_entry = sum % l

    if new_entry not in dict:
        dict[new_entry] = 0
    dict[new_entry] += 1

total_count = 0

for key in dict:
    if (key + l/3) in dict and (key + (2*l)/3) in dict:
        total_count += (dict[key] * dict[key + l/3] * dict[key + (2*l)/3])

print(total_count)