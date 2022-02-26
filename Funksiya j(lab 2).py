#Funksiya j(lab 2):
x,y=map(float,input("Enter (x,y) koordinates: ").split(","))
if (y>=1-x and y>=2*x**2 and x<=0) or (y>=1-x and y>=2*x**2 and 0<=x<=1):
    print("Verilen oblasta daxildi")
else:
    print("Verilen oblasta daxil deyil")
    
