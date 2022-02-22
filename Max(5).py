#Max number(out of 5 numbers)
num1,num2,num3,num4,num5=map(int,input("Enter 5 integers: ").split(","))
max_=num1
if max_<num2:
    max_=num2
if max_<num3:
    max_=num3
if max_<num4:
    max_=num4
if max_<num5:
    max_=num5
print(max_)
