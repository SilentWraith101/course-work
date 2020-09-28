count = 0
total = 0
while count < 5:
    count = count + 1
    try:
        number = float(input(f'Enter number{count}: '))
    except:
        print(f'Invalid entry number{count} set to zero')
        number = 0
    if number < 0 or number >= 100:
        print('Number out of range - set to zero')
        number = 0
    total = total + number
        
print('the final value is:',total)




                   
