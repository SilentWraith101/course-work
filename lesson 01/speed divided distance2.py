#input - speed and distnace
speed = float(input("enter the speed in which you were travelling at "))
distance = float(input("enter the distnace you traveled "))

#calculating - time
time = (distance / speed)
hours = int(time)

#calculating the minuetes - approximatly
minuetes = int((time - float(hours)) * 60)

#output - mph
print (time)
print (hours)
print (minuetes)
print (f"it will take you approximately {hours}hour(s) {minuetes}mins to reach your destination")
                 
