num = int(input())
array = input().split(" ")
array = list(map(int, array))

array.sort()

highest_index = 0
for index, number in enumerate(array):

    if number <= len(array)-index:
        highest_index = max(highest_index, number)

highest_found_index = num

while highest_found_index >= highest_index:
    if (highest_found_index == highest_index):
        break
    if (array[num-highest_found_index])>=highest_found_index:
        break
    highest_found_index-=1


print(highest_found_index)