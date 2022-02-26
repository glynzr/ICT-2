#Task 8(lab 2):
x,y=map(float,input("Enter (x,y) koordinates: ").split(","))
if (x**2+y**2<=1 and x<=0 and y>=0) or (x**2+y**2<=1 and x>=0 and y<=0) or (y<=1-x and x>=0 and y>=0):
    print("Verilen oblasta daxildi")
else:
    print("Verilen oblasta daxil deyil")
