import imp


import json
filename = "python_work/fav.json"
favorite_number = []
number = input("What is your favorite number?")
while True:
    try:
        number_int = int(number)
    except ValueError:
        number = input("You input is not a number,Please retype!")
    else:
        favorite_number.append(number)
        break
print(favorite_number)    
try:
    with open(filename,"w") as file_object:
        json.dump(favorite_number,file_object)
except FileNotFoundError:
    pass
else:
    print("I had marked your favorite number!")



