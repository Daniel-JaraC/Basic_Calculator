num = input("""Select the operation you wish to perform
        1: Addition
        2: Subtraction
        3: Multiplication
        4: Division\n""")

if num == '1':
    print("Type 2 numbers you wish to add.\n ")
    a, b = input(), input()
    res = float(a) + float(b)
    print(a + " + " + b + " = " + str(res))
elif num == '2':
    print("Type 2 numbers you wish to subtract.\n ")
    a, b = input(), input()
    res = float(a) - float(b)
    print(a + " - " + b + " = " + str(res))
elif num == '3':
    print("Type 2 numbers you wish to multiply.\n ")
    a, b = input(), input()
    res = float(a) * float(b)
    print(a + " * " + b + " = " + str(res))
elif num == '4':
    print("Type 2 numbers you wish to divide.\n ")
    a, b = input(), input()
    try:
        res = float(a) / float(b)
        print(a + " / " + b + " = " + str(res))
    except ZeroDivisionError:
        print("Cannot divide by 0.\n ")
else:
    print("Invalid operation.\n ")

print("Thank you.\n")
