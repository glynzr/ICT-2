#Task 9(lab 2):
x,y=map(float,input("Enter (x,y) koordinates: ").split(","))
if (y<=-x+4 and y>=1/x and x>0) or (y>=-x-4 and y<=-1/x and x<0):
    print("Verilen oblasta daxildi")
else:
    print("Verilen oblasta daxil deyil")
