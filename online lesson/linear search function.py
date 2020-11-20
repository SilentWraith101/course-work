def linear_search(myList,item):
    for i in range(len(myList)):
        if myList[i]==item:
            return i
    return -1

myList = [918,7,12,5,15,10,3]
print("Element in List :", myList)
x = int(input("Enter searching element :"))

result = linear_search(myList,x)
if result==-1:
    print("Element not found in the list")
else:
    print( "Element " + str(x) + " is found at position %d" %(result))
