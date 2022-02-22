#Task 2 (1st mmethod)
num1,num2,num3=map(float,input("Enter 3 numbers: ").split(","))
if num1==num2 and num2==num3:
    print("The sum of the 3 numbers is {}".format(num1*3))
else:
    print("The sum of 3 numbers is {}".format(num1+num2+num3))
 #Task 2 (2nd method)
a,b,c=map(float,input("Enter 3 numbers: ").split(","))
if a!=b and b!=c and a!=c:
    print("The sum of the 3 numbers is {}".format(a+b+c))
elif a==b and b==c :
    print("The sum of the 3 numbers is {}".format(a*3))
