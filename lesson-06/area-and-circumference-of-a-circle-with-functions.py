pi = 3.14


def main():
    radius = get_float('Enter the radius: ', 10.0, 100.0)
    print('Area of the circle is: ', circle_area(radius))
    print('Circumference of the circle is: ', circle_circumference(radius))


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


def circle_area(radius):
    return pi * (radius ** 2)


def circle_circumference(radius):
    return (2 * pi) * radius


main()
