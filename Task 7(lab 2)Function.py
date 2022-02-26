#Function 7(lab 2):
x,y=map(float,input("Enter (x,y) koordinates: ").split(","))
if (-1<=x<=0 and 0<=y<=1) or (y>=x and x**2+y**2<=1 and x>=0) or (x<=0 and x**2+y**2<=1 and y>=x):
    print("Verilen oblasta daxildi")
else:
    print("Verilen oblasta daxil deyil")
    
    
