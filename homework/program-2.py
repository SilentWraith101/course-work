file_name = input('What file do you want to read from? ')

search_value = int(input('Enter the value you want to search for: '))

try:
    handler = open(file_name, 'r')
    numbers = handler.read().strip(',').split(',')
    handler.close()
    # Making a variable for length
    length = len(numbers)

    # Converting all the strings within the list to integers
    for i in range(0, length):
        numbers[i] = int(numbers[i])
except FileNotFoundError:
    numbers = []


# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
            # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
            # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        # Element is not present in the array
        return -1


result = binary_search(numbers, 0, len(numbers)-1, search_value)
if result == -1:
    print('Value does not exist in file.')
else:
    print('Value does exist.')
