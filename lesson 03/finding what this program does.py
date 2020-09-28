a = 0
b = 1
count = 0
max_count = 20
while count < max_count:
    count = count + 1
    old_a = a
    print(old_a)
    a = b;
    b = old_a + b
print('end')
