#entering the values - height, length, width
height = float(input("Enter the height: "))
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))



#calclulating results - surface area and volume
area = (height*length*2)+(length*width*2)+(width*height*2)
volume = (height * width *length)

#outputing results - surface area and volume
print("The surface area of your cuboid is: ", area)
print("The volume of your cuboid is: ", volume)
