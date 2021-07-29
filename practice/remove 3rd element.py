num = [10,20,30,40,50,60,70,80,90]
i = 0
every3 = 0
while num:
    #print("while loop")
    i += 1
    #print("i: ", i)

    every3 += 1
    #print("every3: ", every3)

    if every3 % 3 == 0:
        #print("if statement 1: ")
        print(num.pop(i - 1))
        every3 = 0
        i -= 1
        #print("Every3: ", every3, "i:", i)

    if i > len(num)-1 :
        i = 0
        #print("If statement 2: ")
        #print("Length: ", (len(num)-1), "i:", i)

