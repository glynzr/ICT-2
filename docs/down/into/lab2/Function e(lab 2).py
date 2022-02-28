#Funksiya e (lab 2):
x,y=map(float,input("Enter (x,y) coordinates: ").split(","))
if (x**2+y**2<=1 and x>=0) or (x**2+y**2<=1 and y>=-x and x<=0) or (y<=x and x**2+y**2<=1 and x<=0):
    print("Verilen oblasta daxildi")
else:
    print("Verilen oblasta daxil deyil")
