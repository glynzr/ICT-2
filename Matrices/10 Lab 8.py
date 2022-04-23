#10 Lab 8
from random import randint
while True:
    n=int(input("n= "))
    if n>0:
        break
A=[]
for i in range(n):
    A+=[[randint(-10,10) for _ in range(n)]]
    for t in A[i]:
        print("{:2d}".format(t),end=" ")
    print()
a_min,b_min=0,0
for x in range(n):
    for y in range(n):
        if A[x][y]<A[a_min][b_min]:
            a_min,b_min=x,y
su=0
for z in range(n):
    su+=A[z][b_min]
print(su)
