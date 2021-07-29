n = int(input("Enter the no. of rows: "))

for i in range(n, 0, -1):
    for j in range(n-i):
        print(end=" ")
    for j in range(1, i+1):
        print("*", end=" ")
    print()


