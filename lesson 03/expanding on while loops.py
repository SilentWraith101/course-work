# Giving variables a and s values
a = 1
s = 0
print('Enter numbers to add  to the sum.')
print('Enter 0 to quit.')
# While loop to check wether the value they have entered is 0
while a != 0:
    print('Current Sum:',s)
    # Asking the user for a value
    a = float(input('Number?'))
    # Calculating the new value 
    s = s + a
# Outputing the final result
print('Total Sum =',s)
