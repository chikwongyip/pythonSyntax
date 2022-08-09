
def write_file(filename,content):
    with open(filename,"a") as file_object:
        file_object.writelines(content)