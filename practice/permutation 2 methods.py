# permutation of a given list
# the number of cases is n!

# define a function, this function use lots of RAM

def perm1(lst):

    # base cases

    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:

        # we are storing one item in the list l and apply the recursion on the rest list

        l = []

        # iterating through the given list
        for i in range(len(lst)):

            # kick out one item at a time and store that in a variable x.

            x = lst[i]

            # add rest of the items but not the kicked one into a list xs.

            xs = lst[:i] + lst[i+1:]

            # now if we apply recursion on xs, we will end up with p
            # as a new kicked out element, which can be stored in list l.

            for p in perm1(xs):
                l.append([x]+p)
        return l


# second code to use as a generator by using yield instead of return
# this method will use less RAM


def perm2(lst):

    # base cases

    if len(lst) == 0:
        yield 
    elif len(lst) == 1:
        yield lst
    else:

        for i in range(len(lst)):

            # kick out one item at a time and store that in a variable x.

            x = lst[i]

            # add rest of the items but not the kicked one into a list xs.

            xs = lst[:i] + lst[i+1:]

            # now if we apply recursion on xs, we will end up with p
            # as a new kicked out element, which can be stored in list l.

            for p in perm2(xs):
                yield [x] + p



# converting string data into list data

data = list('aieou')

print("Results of Perm 2 function: ")

# now result is stored in l, but still need to join all the individual items
# print all the lines one by one

for r in perm2(data):
    print(r)

















