def get_integer(prompt, lower=0, upper=100000):
    """
    Function to input an integer value, the function test for a valid
    integer.
    Expects a prompt in the form of a string.
    Returns a valid integer or the value 0 if there is an error.
    """
    while True:
        try:
            number = int(input(prompt))
        except:
            number = 0
        if number >= lower and number <= upper:
            return number
        else:
            print(f'''######Error - value out of range, needs to be in 
                    the range {lower} to {upper}#####''')


num = get_integer('Enter an integer: ')
print(num)
