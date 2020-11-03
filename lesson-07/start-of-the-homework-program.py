paint = 2.00
carpet = 1.00

windows = int(input('How many numbers do you want in the sum?'))
total = 0
i = 0
while i < count:
    window_length = float(input('Enter the length of the window: '))
    window_width = float(input('Enter the width of the window: '))
    print('Window area equals


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
