#input
test1 = float(input("Enter a value"))
#stating what operator is in use 'And'
print("And Operator")
#And calculations 
if test1 > 85.0 and test1 < 86.5:
    print ("measurement is in range")
else:
    print ("measurement is out of range")
#stating what operator is in use 'Or'
print("Or Operator")
#Or calculations
if test1 < 85.0 or test1 > 86.5:
    print ("measurement is out of range")
else:
    print ("measurement is in range")



