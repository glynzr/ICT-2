#slide 105 Task B
from random import randint
A=[randint(0,5) for i in range(10)]
print(A)
li=[]
for x in range(len(A)-1):
    if A[x]==A[x+1]:
        if A[x] not in li:
            li+=[A[x]]
if len(li)!=0:
    print("Tapildi: ",*li,end=" " )
else:
    print("Tapilmadi!")
