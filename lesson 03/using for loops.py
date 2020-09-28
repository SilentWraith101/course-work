count = int(input('How many numbers do you want in the sum?'))
total = 0
for i in range (count):
    print('Current Value:',total)
    numbers = float(input('Numbers?'))
    total = total + numbers
    
print('Final result =',total)
     
