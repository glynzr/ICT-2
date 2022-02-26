#Funksiya 1 (Lab2):
x,y=map(float,input("Enter (x,y) koordinates: ").split(","))
if (y<=-x and y>=x**2-2 and x<=0) or (y>=x**2-2 and x>=0 and y<=x):
    print("Verilen oblasta daxildi")
else:
    print("Verilen oblasta daxil deyil")
