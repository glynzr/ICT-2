#Task b(slide 54):
import math
x,y=map(float,input("Enter (x,y)koordinates: ").split(","))
if y<=0.5 and y>=0 and 0<=x<=math.pi:
    print("Oblasta daxildi")
else:
    print("Oblasta daxil deyil")
