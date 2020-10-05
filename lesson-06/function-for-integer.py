def get_integer(prompt):
    """
    Function to input an integer value, the function test for a valid
    integer.
    Expects a prompt in the form of a string.
    Returns a valid integer or the value 0 if there is an error.
    """
    try:
        number = int(input(prompt))
    except ValueError:
        number = 0
    return number


num = get_integer('Enter an integer: ')
print(num)
