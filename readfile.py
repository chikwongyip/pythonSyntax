filename = "python_work\learning_python.txt"
with open(filename) as file_object:
    content = file_object.read()
    print(content)
file_object.close()

with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())
file_object.close()
with open(filename) as file_object:
    str_message = ''
    lines = file_object.readlines()
    for line in lines:
        str_message = str_message + line.rstrip()
    
    print(str_message)
file_object.close()