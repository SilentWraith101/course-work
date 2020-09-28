# Start of the program
while True:
    # Errot trapping using a try and excpet
    try:
        # Asking the user for an input
        number = int(input('Enter a number: '))
    except:
        number = 0
        # Using if to check if the number entered by the user is within a range
    if number in range (10,21):
        # Breaking out of the loop
        break
    else:
        print('#######The Number is not within the range 10 - 20#######')

# Printing the final result if the number is within range
print('Number accepted =',number)
