#Task c(slide 54):
x,y=map(float,input("Enter (x,y) koordinates: ").split(","))
if (x**2+y**2==1 and x<=0) or (x**2+y**2<1 and y>=x):
    print("Oblasta daxildi")
else:
    print("Oblasta daxil deyil")
