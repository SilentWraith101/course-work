while True:

    # Outputing the option you can choose
    print('Option 1: Addition, Option 2: Subtraction, Option 3: Multiplication, Option 4: Division, Option 5: Quit')

    option = int(input('What option do you want to use? '))

    # If statement for addition
    if option == 1:
        value1 = float(input('Enter number 1: '))
        value2 = float(input('Enter number 2: '))
        total = value1 + value2
        print(total)

    # If statement for subtraction
    if option == 2:
        value1 = float(input('Enter number 1: '))
        value2 = float(input('Enter number 2: '))
        total = value1 - value2
        print(total)

    # If statement for multiplication
    if option == 3:
        value1 = float(input('Enter number 1: '))
        value2 = float(input('Enter number 2: '))
        total = value1 * value2
        print(total)

    # If statement for division
    if option == 4:
        value1 = float(input('Enter number 1: '))
        value2 = float(input('Enter number 2: '))
        total = value1 / value2
        print(total)

    # If statement for addition
    if option == 5:
        print('End program')
        break


