count = int(input('How many numbers do you want in the sum?'))
total = 0
i = 0
while i < count:
    print('Current Value:',total)
    numbers = float(input('Numbers?'))
    total = total + numbers
    i = i + 1

print('Final result =',total)
     
