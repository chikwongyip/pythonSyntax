print("give me two number, and I will divide them")
print("Enter 'q' to quit")

while True:
    first_number = input("\n Frist number")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can divide two by 0")
    else:
        print(answer)