#Task 7
price=float(input("Enter the value of the product: "))
if price<=1000:
    print("There is no change in the price")
else:
    print("There is a 10% discount in the price and it will be {}".
          format(price-(price*10)/100))
