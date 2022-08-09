filename = "happpy.txt"
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print(filename + "Not exist!")