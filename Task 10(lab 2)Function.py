#Task 10(lab 2):
x,y=map(float,input("Enter (x,y) koordinates: ").split(","))
if (y>=x**2 and y<=1) or (y<=-x**2 and y>=-1):
    print("Verilen oblasta daxildi")
else:
    print("Verilen oblasta daxild deyil")
