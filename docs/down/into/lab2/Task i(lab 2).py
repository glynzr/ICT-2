#Task i(lab 2):
x,y=map(float,input("Enter (x,y) koordinates: ").split(","))
if x**2+y**2<=1 or (x**2+y**2>=1 and 0<=y<=1 and 0<=x<=1):
    print("Verilen oblasta daxildi")
else:
    print("Verilen oblasta daxil deyil")
