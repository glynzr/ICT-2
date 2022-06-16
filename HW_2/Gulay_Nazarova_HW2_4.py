#Task D
A=[]
while True:
    a=input("Enter a number(blank to quit):")
    if a!=" ":
        A+=[int(a)]
    if a==" ":
        break
print(A)


flag=True
for i in range(len(A)-1):
    for j in range(i+1,len(A)):
        if A[i]>A[j]:
            flag=False
            break



if flag==False:
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            if A[i]<A[j]:
                flag="none"
                break

if flag==True:
    print("A list is ascendingly sorted")
elif flag==False:
    print("A list is descendingly sorted")
else:
    print("A list is unsorted")
 
