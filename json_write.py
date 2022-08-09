import json
filename = "python_work/number.json"
numbers = [2,3,4,5,7]
try:
    with open(filename,"w") as file_object:
        json.dump(numbers,file_object)
except FileNotFoundError:
    pass
