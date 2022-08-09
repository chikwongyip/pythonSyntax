import numbers


import json
filename = "python_work/number.json"
with open(filename) as file_object:
    number = json.load(file_object)
print(number)
