#Task D (slide 54):
x,y=map(float,input("Enter (x,y) koordinates: ").split(","))
if (y<=2-x and y<=x**2 and 0<=x<=2) or (y>=2-x and y<=x**2 and x<=-2):
    print("Verilen oblasta daxildi")
else:
    print("Verilen oblasta daxil deyil")
