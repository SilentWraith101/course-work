# Asking the user for a value to assign to the variables
number = int(input('Enter the number you want to be multiplied: '))
count = int(input('Enter the number you want to be multiplied: '))
# Making total equal 0
total = 0

# For loop to make the value times by the 2nd variable with addition
for i in range(count):
    total += number
# i = 0
# while i < count:
#     i += 1
#     total += number

print('Final result =', total)
