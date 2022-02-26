#Exercise 37:Name that shape
shape=["triangle","quadrilateral","pentagon",
       "hexagon","octagon","nonagon","decagon"]
x=int(input("Enter number of sides:  "))
if 3<=x<=10:
    if x==3:
        print("If the figure has {} sides,it is {}.".format(x,shape[0]))
    elif x==4:
        print("If the figure has {} sides,it is {}.".format(x,shape[1]))
    elif x==5:
        print("If the figure has {} sides,it is {}.".format(x,shape[2]))
    elif x==6:
        print("If the figure has {} sides,it is {}.".format(x,shape[3]))
    elif x==7:
        print("If the figure has {} sides,it is {}.".format(x,shape[4]))
    elif x==8:
        print("If the figure has {} sides,it is {}.".format(x,shape[5]))
    elif x==9:
        print("If the figure has {} sides,it is {}.".format(x,shape[6]))
    elif x==10:
        print("If the figure has {} sides,it is {}.".format(x,shape[7]))
else:
    print("Invalid data")
    
