#Qrafik A (slide 54):
x,y=map(float,input("Enter (x,y)koordinates: ").split(","))
if x**2+y**2>4 and y<=x and x<=2:
    print("Verilen oblasta daxildi")
else:
    print("Verilen oblasta daxil deyil")
