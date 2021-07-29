# combination of 3 digits

def combi(lst):
    for i in lst:
        for j in lst:
            for k in lst:
                print(i,j,k)


combi([1,2,3])