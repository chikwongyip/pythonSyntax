from write_file import write_file
reason = input("Why you like programming")
filename = "python_work/programmer.txt"
while reason != " ":
    write_file(filename, reason)
