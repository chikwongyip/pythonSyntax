"""vistor list"""
def write_file(filename, username):
    with open(filename, "a") as file_object:
        file_object.writelines(username + "welcome to disney")
username = input("Type your name:")
filename = "python_work/guest_book.txt"
while username != " ":
    write_file(filename, username)



