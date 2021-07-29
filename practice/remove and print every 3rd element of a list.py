l = input("Enter the list of number separated by commons: ")
int_list = l.split(" ")


def remove_nums(data):

    # List start with index zero
    idx = 0

    # Position of number in form of index.
    position = 3-1

    # Length of list
    len_data = len(data)

    # Logic when the length of list is > 0, only than do the process
    loop = 0

    while len_data > 0:
        loop += 1
        print("\nLoop: ", loop)
        idx = (position + idx)%len_data
        len_data -= 1
        print("\nRemoved item: ", data.pop(idx))
        print("Length:", len_data, "idx:", idx, "\nList: ", data)



print(remove_nums(int_list))
























