#Exercise 35:Dog years
humanyear=float(input("Enter human years: "))
if humanyear<0:
    print("Error!!!!")
elif humanyear<2:
    print("{}human year =10.5 dog years".format(humanyear))
elif humanyear>=2:
    dogyear=10.5+(humanyear-2)*4
    print("{} human years={} dog years".format(humanyear,dogyear))
                                               
