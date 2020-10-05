a = 23
b = -23


# It will check if the absolute value of both a and b are equal
def absolute_value(n):
    if n < 0:
        n = -n
    return n
    # return n if n > 0 else -n


# Checking if the absolute value of a is equal to b
if absolute_value(a) == absolute_value(b):
    print('The absolute values of', a, 'and', b, 'are equal')
else:
    print('The absolute values of', a, 'and', b, 'are different')
