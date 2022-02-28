#Task A (slide 55)
x,y=map(float,input("Enter (x,y) koordinates: ").split(","))
if (y<=x**2 and y>=2-x) or (y>=x**2 and y>=4-x**2 and x>=0) or (y<=2-x and y>=x**2 and y<=4-x**2 and x<=0) or (y<=x**2 and y<=2-x and x>=0):
    print("Verilen oblasta daxildi")
else:
    print("Verile oblasta daxil deyil")
