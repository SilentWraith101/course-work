Number_Amount = int(input('Enter the amount of values you want to enter: '))


def writefile(value):
    with open('class_exercise.txt','a') as fout:
        fout.write(f'{value},')


# section to input data
for i in range(Number_Amount):
    data = int(input('Enter value: '))
    writefile(data)
