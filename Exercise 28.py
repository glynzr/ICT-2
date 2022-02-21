#Exercise 28: Wind Chill
Ta=float(input("Enter the air temperature in Celcius degree :"))
V=float(input("Enter the wind speed in kilometres per hour: "))
if Ta<=10 and V>4.8:
    WCl=13.12+0.6215*Ta-11.37*(V**0.16)+0.3965*Ta*(V**0.16)
    print("Wind chill={:.2f}".format(WCl))
else:
    print("Invalid data")
