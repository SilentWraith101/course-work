file_name = input('What do you want the name of the file to be? ')

number_amount = int(input(
    'Enter the amount of values you want to enter: '
))

try:
    handler = open(file_name, 'r')
    numbers = handler.read().strip(',').split(',')
    handler.close()
    # Making a variable for length
    length = len(numbers)

    # Converting all the strings within the list to integers
    for i in range(0, length):
        numbers[i] = int(numbers[i])
except FileNotFoundError:
    numbers = []

# Section to input data
for i in range(number_amount):
    data = int(input('Enter value: '))
    numbers.append(data)

# Converting to a set removes duplicates
numbers = list(set(numbers))
numbers.sort()

length = len(numbers)
# Converting all the strings within the list to strings
for i in range(0, length):
    numbers[i] = str(numbers[i])

numbers = ",".join(numbers)

# Writing to the file using 'w' compared to 'a' which appends
with open(file_name, 'w') as handler:
    handler.write(numbers)
