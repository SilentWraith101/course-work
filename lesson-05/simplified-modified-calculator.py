def calculate(operation, number1, number2):
    if operation == 1:
        return number1 + number2
    elif operation == 2:
        return number1 - number2
    elif operation == 3:
        return number1 * number2
    elif operation == 4:
        return number1 / number2


while True:

    # Outputting the option you can choose
    print('Option 1: Addition, Option 2: Subtraction, Option 3: Multiplication, Option 4: Division, Option 5: Quit')

    option = int(input('What option do you want to use? '))

    if option >= 1 and option <= 4:
        print(calculate(
            option,
            float(input('Enter number 1: ')),
            float(input('Enter number 2: '))
        ))

    # If statement for addition
    if option == 5:
        print('End program')
        break