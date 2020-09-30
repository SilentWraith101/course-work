# Assigning a value to pi
pi = 3.14


# Doing a while loop to check that the value entered for radius is within the range 6 to 20
while True:
    radius = int(input('Enter the radius of the circle: '))
    # If statement to check that the values are within the range
    if radius >= 6 and <= 20:
        break
    print('#####Valid value in the range 6 to 20#####')

print(f'Radius value {radius} accepted')


# Doing a while loop to check that the value entered for height is within the range 6 to 30
while True:
    height = int(input('Enter the height of the cylinder: '))
    # If statement to check that the values are within the range
    if height >= 6 and <= 30:
        break
    print('#####Valid value in the range 6 to 30#####')

print(f'height value {height} accepted')


# Calculations to get the values for circleArea, surfaceArea and volume
circleArea = pi * (radius ** 2)
surfaceArea = (pi * 2) * (radius ** 2)+(pi * 2) * (radius) * (height)
volume = circleArea * height

# Outputing the results
print(f'The surface area of the cylinder is {surfaceArea}')
print(f'The volume of the cylinder is {volume}')
