#Task 12 (lab 2):
x,y=map(float,input("Enter (x,y) koordinates: ").split(","))
if -2<=y<=0 and x**2+y**2>=4 and y<=x and x<=0:
    print("Verilen oblasta daxildi")
else:
    print("Verilen oblasta daxil deyil")
