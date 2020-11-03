# Opening and reading the file
# Also stripping and splitting the the values within the file
file_demo = open('class_exercise.txt', 'r')
numbers = file_demo.read().strip(',').split(',')
file_demo.close()

# Making a variable for length
length = len(numbers)

# Converting all the strings within the list to integers
for i in range(0, length):
    numbers[i] = int(numbers[i])

# Getting the total value and the average of the total
total = sum(numbers)

print('Total:', total)
print(f'Average: {total / length:.2f}')
