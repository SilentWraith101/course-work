currentNumber = 0
newNumber = 1
count = 0
max_count = 20
for i in range (max_count):
    count = count + 1
    old_number = currentNumber
    print(old_number)
    currentNumber = newNumber;
    newNumber = old_number + newNumber
print('END')
