""" This program will enable us to know the frequency of letters used
to write the sign board."""

# user inputs
what_to_write = input('Enter the text which you want write:  ').upper()
what_is_written = input('Enter the text which is already written: ').upper()

all_letters_need = [i for i in what_to_write if i != ' ']
all_letters_have = [i for i in what_is_written if i != ' ']


def get_freq(lst):
    f = {}
    for i in lst:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    return f


# print(get_freq(all_letters_need))
# print(get_freq(all_letters_have))

A = get_freq(all_letters_need)
B = get_freq(all_letters_have)

for k, v in A.items():
    if k in B.keys():
        # print(k, ' ', v)
        A[k] = v - B[k]

for k, v in A.items():
    if v > 0:
        print(f'{k} ---> {v}')
