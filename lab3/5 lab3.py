#5 lab3
#1st method
A,B=map(int,input("Enter two integers: ").split(","))
even=0
n=B+1-A
for x in range(A,B+1):
    if x%2==0:
        even+=1
    A+=1
print("There are {} even numbers".format(even))
odd=n-even
print("There are {} odd numbers".format(odd))



#2nd method
A,B=map(int,input("Enter two integers: ").split(","))
n=B-A+1
even=0
while A<=B:
    if A%2==0:
        even+=1
    A+=1
print(even)
odd=n-even
print(odd)
        
