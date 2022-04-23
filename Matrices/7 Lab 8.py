#7 Lab 8
from random import randint
while True:
    n=int(input("n= "))
    if n>0:
        break
A=[]
for i in range(n):
    A+=[[randint(-10,10) for _  in range(n)]]
    for t in A[i]:
        print("{:3d}".format(t),end=" ")
    print()
su=0
for a in range(n):
    su+=A[a][a]

for x in range(n):
    for y in range(n):
        if x%2!=0:
            A[x][y]=A[x][y]/su



print("\n\n")

for z in range(n):
    for  d in A[z]:
        print("{:4.2f}".format(d),end=" ")
    print()
        
        
