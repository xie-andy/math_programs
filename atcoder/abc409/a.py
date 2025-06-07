num = int(input())
array1 = input()
array2 = input()

for i in range(0, num):
    
    if array1[i] == 'o' and array2[i] == 'o':
        print("Yes")
        exit()

print("No")

