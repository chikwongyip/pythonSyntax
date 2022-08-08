username = input("请输入用户姓名:")
filename = "python_work\guest.txt"

with open(filename,"a") as file_object:
    file_object.writelines(username)


