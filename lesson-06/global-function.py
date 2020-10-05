a = 0


def print_func():
    global a;
    print 'In print_func a =', a;
    a = 17;
    print 'In print_func a =', a;


print_func()
print 'in the variable a =', a;