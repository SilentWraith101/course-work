def get_float(prompt, lower=0.0, upper=1000000000.0):
    """ Function to input an integer value, the function test for a
    valid integer.
    expects a prompt in the form of a string
    returns a valid integer or the value 0 if there is an error
    """
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


def get_perimeter(x, y):
    return (x + y) * 2


def get_rect_area(x, y):
    ''' Function to calculate the area of a rectangle.
    Inputs - length and width.
    '''
    return x * y


length = get_float("Enter the length: ", 0.0, 1000.0)
width = get_float("Enter the width: ", 0.0, length)
perimeter = get_perimeter(length, width)
area = get_rect_area(length, width)
print('The perimeter of the rectangle is: ', perimeter)
print('The area of the rectangle is: ', area)
