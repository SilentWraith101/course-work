#input
try:
    spend = float(input("Enter the total amount spent: "))
    discount = float(0.00)
except:
    print("Total money spent set to £0")
    spend = 0
#calculations
if spend > 100:
    discount = (spend * 0.10);
    print("You have earned a discount of:£",discount)

#output

print(f"Total to pay is: £{spend-discount:0.2f}")

#to round to 2 decimal places you have to put an f at the start of the brackets and then put the variable/s within {}
#and a colon with the set number of decimal places after

#how to lay out a decimal round print statement
#print(f"sentance: £{variable:0.number of decimal placesf}")
