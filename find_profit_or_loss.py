orginal_price=float(input("Enter the Product's Orginal Price: "))
selling_price=float(input("Enter the Product's Selling Price: "))
if(orginal_price>selling_price):
    loss=orginal_price-selling_price
    print("Your Loss is: ",loss)
elif(selling_price>orginal_price):
    profit=selling_price-orginal_price
    print("Your Profit is: ",profit)
else:
    print("Oopsh...!,No Profit of Loss Found")