#slide 122 Task A
from random import randint
while True:
    N=int(input("N= "))
    if N>0:
        break
li=[randint(-10,10) for _ in range(N)]
print(li)
l=[x for x in li if x%2==0 and x<0]
print(l)
