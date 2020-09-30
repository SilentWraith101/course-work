# It will return the result of a calculation based on an operator number
# 1 - 4 which correspond to addition, subtraction, multiplication and
# division.
def calculate(operation, number1, number2):
    if operation == 1:
        return number1 + number2
    elif operation == 2:
        return number1 - number2
    elif operation == 3:
        return number1 * number2
    elif operation == 4:
        return number1 / number2


runningTotal = False

while True:

    # Outputting the option's you can choose
    print('''Options
    1: Addition
    2: Subtraction
    3: Multiplication
    4: Division
    5: Quit''')

    option = int(input('What option do you want to use? '))

    if option >= 1 and option <= 4:
        total = calculate(
            option,
            runningTotal if runningTotal else float(input('Enter number 1: ')),
            float   (input('Enter number 2: '))
        )
        print(f'Total: {total}')

        # Answer variable to see wether they want to save thier total
        answer = str(input('Do you want to continue your calculation y/n?'))

        if answer.lower() == 'y':
            runningTotal = total
        else:
            print('Total not saved')
            runningTotal = False

    # If statement for addition
    if option == 5:
        print('End program')
        break