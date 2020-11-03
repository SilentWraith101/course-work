pi = 3.14159


# Defining main
def main():
    length = get_float('Enter the length: '0.0, 1000)
    height = get_float('Enter the height: '0.0, 1000)
    width = get_float('Enter the width: '0.0, length)
    print('volume of the cuboid is: ', cuboid_volume(length, height, width))
    print('Surface area of the cuboid is: ', cuboid_surface_area(length, height, width))


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


# Function for the surface area of a cuboid
def cuboid_surface_area(length, width, height):
    # Function to calculate the total surface area of the cuboid
    return (length *width) * 2 + (length * height) * 2 + (height * width) * 2


def cuboid_volume(length, width, height):
    # Function to calculate the volume of the cuboid
    return (length * width * height)


# Calling the main function
main()
