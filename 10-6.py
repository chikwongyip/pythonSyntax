print("Please type two number")
while True:
    number_1 = input("Please input number 1")
    number_2 = input("Please input number 2")
    try:
        number_int_1 = int(number_1)
        number_int_2 = int(number_2)
    except TypeError:
        number_1 = input("number 1 is not a number,Please re-input")
        number_2 = input("number 1 is not a number,Please re-input")
    else:
        result = number_int_1 + number_int_2
