spend = float(input("Enter the total amount spent: "))
discount = float(0.00)
if spend > 100:
    discount = spend * 0.10;
    print("You have earned a discount of:£",discount)

print("Total to pay is: £",spend-discount)
