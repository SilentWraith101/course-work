number_amount = int(input(
    'Enter the amount of values you want to enter: '
))


def write_file(value):
    with open('class_exercise.txt', 'a') as fout:
        fout.write(f'{value},')


# section to input data
for i in range(number_amount):
    data = int(input('Enter value: '))
    write_file(data)
