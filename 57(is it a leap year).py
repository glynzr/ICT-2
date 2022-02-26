#Exercise 57:Is it a leap year? (1st method)
year=int(input("Enter the year: "))
if year%4==0:
    print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))

#2nd method:
x=int(input("Enter a year: "))
if x%400==0:
    print("{} is a leap year".format(x))
elif x%100==0:
    print("{} is not a leap year".format(x))
elif x%4==0:
    print("{} is a leap year".format(x))
else:
    print("{} is not a leap year".format(x))
