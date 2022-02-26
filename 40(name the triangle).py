#Exercise 40:Name that triangle
a,b,c=map(float,input("Enter length of all sides of trangle: ")
          .split(","))
if abs(a-b)<c<(a+b) and abs(b-c)<a<(c+b) and abs(a-c)<b<(a+c):
    if a==b and b==c:
        print("This is an equilateral triangle")
    elif (a==b and b!=c) or (a==c and b!=c) or (c==b and a!=c)  :
        print("This is an isosceles triangle")
    elif a!=b and b!=c and a!=c:
        print("This is a scalene triangle")
else:
    print("Invalid data")
            
