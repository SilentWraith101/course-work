name = input("Enter Your Name:")
try:
    year = input("Enter the year of your birth:")
    age = 2025 - int(year)
except:
    print("error entering year")
    age = 0
print("Your name is: ",name)
print("in 2025 you will be",age,"years old.")
