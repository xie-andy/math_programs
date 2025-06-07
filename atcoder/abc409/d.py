num_cases = int(input())

result = []

def shift(s, index1, index2):

    char = s[index1]
    s = s[:index1] + s[index1+1:]
    s = s[:index2+1] + char + s[index2+1:]

    return s

for num in range(num_cases):
    length = int(input())
    s = input()

    result.append([])
    
    for i in range(0, length-1):
        
        # keep moving it under we are less than
        if s[i+1] < s[i]:
            bad_char = s[i]
            k = i + 1
            while k < length and s[k] <= bad_char:
                k += 1

            possible = shift(s, i, k-2)

            result[num].append(possible) 
            break

    if len(result[num]) == 0:
        result[num] = [s]
    
for array in result:
    array.sort()
    print(array[0])
