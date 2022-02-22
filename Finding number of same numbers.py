#Finding the same numbers(1st method)
a,b,c=map(int,input("Enter 3 integers: ").split(","))
if a!=b and a!=c and b!=c:
    print("No equal numbers")
elif not(a==b)or(not(b==c or a==c)):
    print("2 numbers are equal")
elif a==b and b==c:
    print("All numbers are equal")


#2nd method
if a==b and b==c:
    print("All numbers are equal")
elif a==b or a==c or b==c:
    print("2 numbers are equal")
