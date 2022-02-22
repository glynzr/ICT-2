#Task 5
import random
a=int(input("a: "))
b=int(input("b: "))
num1=random.randint(a,b)
num2=random.randint(a,b)
num3=random.randint(a,b)
print(num1)
print(num2)
print(num3)
max_=num1
if max_<num2:
    max_=num2
if max_<num3:
    max_=num3
print(max_)



min_=num1
if min_>num2:
    min_=num2
if min_>num3:
    min_=num3
print(min_)


median=(num1+num2+num3)-(max_+min_)
print("The median of 3 random numbers is {}".format(median))
