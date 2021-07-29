num = [3,-1,-7,-4,-5,9,10]

for i in range(1, len(num), 1):
    first = num[i]
    for j in range(i+1, len(num), 1):
        second = num[j]
        for k in range(j+1, len(num), 1):
            third = num[k]
            sum = first + second + third
            if sum == 0:
                print(first, second, third, "\n")



