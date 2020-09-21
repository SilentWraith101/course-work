#input
name = str(input("Enter your name: "))
position = str(input("Enter the position you finished in words: "))
points = 0
prizemoney = 0
#checking thier position and giving them the correct amount of points
if position.lower() == 'first':
    print("you have gained 5 points!")
    points = points + 5
    
if position.lower() == 'second':
    print("you have gained 3 points!")
    points = points + 3

if position.lower() == 'third':
    print("you have gained 1 points!")
    points = points + 1

if position.lower() == 'first':
    points = prizemoney = prizemoney + 10

if position.lower() == 'second':
    points = prizemoney = prizemoney + 7

if position.lower() == 'third':
    points = prizemoney = prizemoney + 4

if position.lower() == 'fourth':
    points = prizemoney = prizemoney + 3

if position.lower() == 'fith':
    points = prizemoney = prizemoney + 2

if position.lower() == 'sixth':
    points = prizemoney = prizemoney + 1



#output
print (name.lower(), points)
print ("You have also won £",prizemoney)


