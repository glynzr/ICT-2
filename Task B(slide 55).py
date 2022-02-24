#Task B(slide 55):
x,y=map(float,input("Enter (x,y) koordinates: ").split(","))
if (x**2+y**2>=1 and y<=0 and y<=x and y<=-x) or (y>=-x and x<=0 and x**2+y**2<=1) or (y>=x and x>=0 and x**2+y**2<=1) or (x**2+y**2<=1 and y>=x and x<=0 and y<=0) or (x>=0 and y<=0 and x**2+y**2<=1 and y>=-x):
    print("Verilen oblasta daxildi")
else:
    print("Verilen oblasta daxil deyil")
