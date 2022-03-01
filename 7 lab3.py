#7 lab3
    #1st method
A=int(input("Enter an integer: "))
B=A
A_=1
while A>0:
    A_*=A
    A-=1
print("{}!={}".format(B,A_))

    #2nd method
A=int(input("Enter an integer: "))
B=A
A_=1
for x in range(1,A+1):
    A_*=x
print(A_)


