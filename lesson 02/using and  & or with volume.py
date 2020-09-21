#input
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
height = float(input("Enter the height: "))
#setting the variable error to false
error = False

#checking length,width and height are in range
if length < 25.5 or length > 26:
    print("Length is out of range range")
    error = True
    
if width < 19 or width > 20:
    print("Width is out of range range")
    error = True

if height < 12 or height > 13:
    print("Height is out of range range")
    error = True

#calculating volume
volume = length * width * height

#output
print ("The volume is: ", volume)

#error validating - if there was an error with any of the values entered for the length,width and height then it will print not valid
if error:
    print("The volume is not valid")
