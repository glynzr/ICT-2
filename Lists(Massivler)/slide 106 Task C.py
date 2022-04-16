#slide 106 Task C
import random
N=int(input("N= "))
A=[random.randint(0,N) for i in range(6)]
li=[]
print(A)
for x in range(len(A)):
    for y in range(x+1,len(A)):
        if A[x]==A[y]:
            if A[x] not in li:
                li+=[A[x]]
if len(li)!=0:
    print("Tapildi: ",*li,end=" ")
else:
    print("Tapilmadi!")
