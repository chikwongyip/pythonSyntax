def read_file(folder, name):
    filename = folder + name
    try:
        with open(filename) as file_object:
            lines = file_object.readlines()
            lv_string = ' '
            for line in lines:
                lv_string = lv_string + line.strip()
    except FileNotFoundError:
        pass
    else:
        return lv_string



