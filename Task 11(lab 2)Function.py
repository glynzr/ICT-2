#Task 11 (lab 2):
x,y=map(float,input("Enter (x,y) koordinates: ").split(","))
if (y<=x and y>=(x-2)**2-3 and y>=0) or (y<=-x and y>=(x-2)**2-3 and y<=0):
    print("Verilen oblasta daxildi")
else:
    print("Verilen oblasta daxil deyil")
    
