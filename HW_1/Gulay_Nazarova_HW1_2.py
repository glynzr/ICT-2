#Task B:Coxbucaqlinin perimetri
import math
x1=input("Enter the x part of the coordinate: ")#baslangic noqtenin koordinati(x)
y1=input("Enter the y part of the coordinate: ")#baslangic noqtenin koordinati(y)
perimeter=0
x_n=0 #en son daxil edilen noqtenin koordinati(x)
y_n=0 #en son daxil edilen noqtenin koordinati(y)
flag=True # daxil edilen koordinat ikinci noqtenin koordinatidirsa True,eks halda False olacaq
a=0 #daxil edilen koordinatlarin sayi
while True:
    x=input("Enter the x part of the coordinate(blank to quit): ")
    a+=1
    if x==" ":
        if a>2:
            perimeter+=math.sqrt((int(x1)-x_n)**2+(int(y1)-y_n)**2) #Bosluq daxil edilenden sonra baslangic noqtenin koordinati ile son daxil edilen koordinat arasindaki mesafe
            perimeter_rounded=round(perimeter,2)
            print("The perimeter of that poligon is {}".format(perimeter_rounded)) 
            print("The perimeter of that poligon is {:.2f}".format(perimeter))#ikinci usul print() ucun 
            break
        else:
            print("Error!!!!!!!")
            break
    y=input("Enter the y part of the coordinate(blank to quit): ")
    if flag==True: #eger daxil edilen ikinci noqtenin koordinatidirsa
        perimeter+=math.sqrt((int(x1)-int(x))**2+(int(y1)-int(y))**2) #baslangic noqtenin koordinati ile ikinci noqtenin koordinati arasindaki mesafe
        flag=False
        x_n=int(x) #en son daxil edilen koordinatlari yadda saxlamaq ucun
        y_n=int(y)
    else:
        perimeter+=math.sqrt((int(x)-x_n)**2+(int(y)-y_n)**2) #qalan noqteler arasindaki mesafe
        x_n=int(x) #en son daxil edilen koordinatlari yadda saxlamaq ucun
        y_n=int(y)





