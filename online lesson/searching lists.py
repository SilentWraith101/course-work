def search(list,x):
    found = 0
    count = len(list)
    for i in range (count):
        if list[i] == x:
            found = found + 1
    return found

list = [9,18,7,12,5,15,10,3]
x = int(input("Enter searching element :"))
print(found)