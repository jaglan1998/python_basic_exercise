# Write a Python function that takes a sequence of numbers
# and determines whether all the numbers are different from each other
# https://www.w3resource.com/python-exercises/python-json-exercise-1.php

x = input("Enter the items of list spaces: ")

A = set(x.split(" "))
B = x.split(" ")

print(A)
print(B)

if len(A) == len(B):
    print("no same values")
else:
    print("some same values")




