#Exercise 45: What color is that square?
column1=["a","c","e","g"]
column2=["b","d","f","h"]
row1=["1","3","5","7"]
row2=["2","4","6","8"]
x=input("Enter column letter: ")
y=input("Enter row number: ")
if (x in column1 and y in row1) or (x in column2 and y in row2):
    print("{}{} is black".format(x,y))
elif (x in column1 and y in row2) or (x in column2 and y in row1):
    print("{}{} is white".format(x,y))
else:
    print("Invalid data")
        
