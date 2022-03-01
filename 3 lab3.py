#3 lab3
    #1st method
A,B=map(int,input("Enter two integers: ").split(","))
c=int(input("Enter an integer: "))
for x in range(A,B+1):
    if x%c==0:
        print(x)

    #2nd method
A,B=map(int,input("Enter two integers: ").split(","))
c=int(input("Enter an integer: "))
while A<=B:
    if A%c==0:
         print(A)
    A+=1
        
    
    
       

       
