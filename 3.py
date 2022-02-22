#Task 3
num1,num2,num3=map(int,input("Enter 3 numbers: ").split(","))
if num1!=num2 and num1!=num3 and num2!=num3:
    print("Sum={}".format(num1+num2+num3))
elif (not(num1==num2)) or (not(num1==num3 or num2==num3)):
    print("Result:0")
