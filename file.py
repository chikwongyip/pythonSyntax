def read_file(folder,name):
    filename = folder + name
    with open(filename) as file_object:
        lines = file_object.readlines()
        lv_string = ' '
        for line in lines:
            lv_string = lv_string + line.strip()
    return lv_string


