import json

j_file = open(input("Input the file name: "))

# print(j_file.read())

py_obj = json.load(j_file)

print("Type of py_obj", type(py_obj))

print(py_obj)

# Now we are converting the above diction into json obj
# save it into a file newjson.json

newjson = json.dumps(py_obj)
f_hand = open("newjson.json", 'w')
f_hand.write(newjson)


