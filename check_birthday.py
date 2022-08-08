filename = "python_work\pi_digits.txt"
with open(filename) as file_object:
    lines = file_object.realines()
    pi_string = " "
    for line in lines:
        pi_string += line.rstrip()
birthday = input("Enter your birthday,in the form mmddyy:")
if birthday in pi_string:
    print("You birthday appears in first million digit of pi!")
else:
    print("You birthday does not appear in first million digits of pis")

