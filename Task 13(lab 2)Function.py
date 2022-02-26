#Task 13 (lab 2):
x,y=map(float,input("Enter (x,y) koordinates: ").split(","))
if (y>=x+2 and x**2+y**2<=25 and x<=0) or (x**2+y**2<=25 and x<=0 and y<=0):
    print("Verilen oblasta daxildi")
else:
    print("Verilen oblasta daxil deyil")
    
