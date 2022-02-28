#Task 8
price=float(input("Enter the price of the product: "))
if price>1000:
    print("Price={}".format(price-(price*5)/100))
elif price>500:
    print("Price={}".format(price-(price*3)/100))
