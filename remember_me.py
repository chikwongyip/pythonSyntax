from asyncio.proactor_events import _ProactorBaseWritePipeTransport
import json
username = input("what is your name: ")
filename = "python_work/username.json"
try:
    with open(filename,"a") as file_object:
        json.dump(username,file_object)
except FileNotFoundError:
    pass
else:
    print("we will remember your name: " + username)

