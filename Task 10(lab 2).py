#Task 10
days=["Monday","Tuesday","Wednesday","Thurday","Friday","Saturday","Sunday"]
x=input("Enter the day of the week (1st letter must be capitalized)")
if x in days:
    if x=days[5]or x=days[6]:
        print("Rest")
    else:
        print("Work")
else:
    print("Invalid data")
