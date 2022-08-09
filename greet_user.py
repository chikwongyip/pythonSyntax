import json
filename = "python_work/username.json"
try:
    with open(filename) as file_object:
        username = json.load(file_object)
except FileNotFoundError:
    pass
else:
    print(username)
    