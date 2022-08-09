from write_file import write_file
filenames = ["python_work/cats.txt", "python_work/dogs.txt","python_work/tiger.txt"]

for filename in filenames:
    try:
        with open(filename) as file_object:
            animals = file_object.readlines()
            for animal in animals:
                write_file()


