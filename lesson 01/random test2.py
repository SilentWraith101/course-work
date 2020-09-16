import random
import string
count = 0
while (count <10000000000000000000000):
    def get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        print("Random string of length", length, "is:", result_str)
get_random_string(4)

count = count + 1
get_random_string(4)
count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1

print "Good bye!"


