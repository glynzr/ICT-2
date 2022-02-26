#Exercise 38: Month Name to Number f days:
months=["january","february","march","april","may","june","july",
       "august","september","october","november","december"]
x=input("Enter the month of the year(all in lowercase): ")
if x in months:
    if x==months[0] or x==months[2] or x==months[4] or x==months[6] or x==months[7] or x==months[9] or x==months[11]:
        print("There are 31 days in {}".format(x))
    elif x==months[1]:
        print("There are 28 or 29 days in {}".format(x))
    else:
        print("There are 30 days in {}".format(x))
else:
    print("Invalid data")
