#Task E(slide 54):
x,y=map(float,input("Enter (x,y) koordinates: ").split(","))
if (x**2+y**2<=1 and 0<=x<=1) or (x**2+y**2>=1 and y>=x-1 and y<=1):
    print("Verilen oblasta daxildi")
else:
    print("Verilen oblasta daxil deyil")
