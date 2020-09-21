#input
spend = float(input("Enter the total amount spent"))

#calculations
try:
    if spend > 100:
        discount = spend * 0.10
        print(f"You have earned a discount of:£{discount:0.2f}")
        
    else:
        discount = 0.00;
        print("You have not qualified for a discount")
except:
    print("Invalid input!")

#output
print(f"Total to pay is:£{spend-discount:0.2f}")
