#slide 119 Task C
from random import randint
#1st method
while True:
    N=int(input("N= "))
    if N>0:
        break
li=[randint(-100,100) for _ in range(N)]
print(li)
li1=[]
li2=[]
count=0
for x in li:
    if x>0:
        li1+=[x]
        count+=1
    else:
        li2+=[x]
print(li1+li2)


#2nd method
from random import randint
while True:
    N=int(input("N= "))
    if N>0:
        break
li=[randint(-100,100) for i in range(N)]
print(li)
count=0
for x in range(len(li)):
    for i in range(x+1,len(li)):
        if li[x]<li[i]:
            li[x],li[i]=li[i],li[x]
print(li)

for t in li:
    if t>0:
        count+=1
print(count)
