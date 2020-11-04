file_name = input('What do you want the name of the file to be? ')

number_amount = int(input(
    'Enter the amount of values you want to enter: '
))


def write_file(value):
    with open(file_name, 'a') as fout:
        fout.write(f'{value},')


# section to input data
for i in range(number_amount):
    data = int(input('Enter value: '))
    write_file(data)
