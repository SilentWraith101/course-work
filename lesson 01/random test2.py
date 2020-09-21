import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)

count = 0
while count < 99:
    print('The count is:', count)
    count = count + 1
    get_random_string(count)

print("Good bye!")
