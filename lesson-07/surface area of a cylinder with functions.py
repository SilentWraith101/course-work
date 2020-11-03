pi = 3.14159


# Defining main
def main():
    radius = get_float('Enter the radius: ', 10.0, 100.0)
    height = get_float('Enter the height: ', 50.0, 300.0)
    #print('Area of the circle is: ', circle_area(radius))
    #print('Circumference of the circle is: ', circle_circumference(radius))
    print('Surface area of the circle is: ', round(cylinder_surface_area(radius, height), 2))


def get_float(prompt, lower=0.0, upper=10000000000.0):
    ''' Function to input an float value, the function test for a
    valid float.
    expects a prompt in the form of a string
    returns a valid float or the value 0 if there is an error
    '''
    while True:
        try:
            number = float(input(prompt))
        except:
            number = 0.00
        if number >= lower and number <= upper:
            return number
        else:
            print(f'''++++++Error - value out of range, needs to be in 
                            the range {lower} to {upper}++++''')


# Function for the area of a circle
#def circle_area(radius):
#    return pi * (radius ** 2)


# Function for circumference of a circle
#def circle_circumference(radius):
#    return (2 * pi) * radius


# Function for the surface area of a cylinder
def cylinder_surface_area(radius, height):
    return (pi * 2) * (radius ** 2)+(pi * 2) * (radius) * (height)


# Calling the main function
main()
