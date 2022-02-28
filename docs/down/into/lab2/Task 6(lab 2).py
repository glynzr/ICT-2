#Task 6: Quadratic equation
import math

a,b,c=map(float,input("Enter the values: ").split(","))
D=b**2-4*a*c


if a==0:
    print("This is not quadratic equation")

    
elif D>0:
    print("This equation has 2 different real solutions")
    x1=(-b+math.sqrt(D))/(2*a)
    x2=(-b-math.sqrt(D))/(2*a)
    print("Result:x1={} and x2={}".format(x1,x2))
    
    
elif D==0:
    print("The equation has 2 equal solutions")
    x=-b/(2*a)
    print("Result:{}".format(x))

    
elif D<0:
    print("The equation does not have real solutions")
