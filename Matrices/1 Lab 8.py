#1 Lab 8
from random import randint
while True:
    n,m=map(int,input("n,m= ").split(","))
    if n>0 and m>0:
        break
A=[]
for i in range(n):
    A+=[[randint(-10,10) for _ in range(m)]]
su=0
for t in range(n):
    for d in A[t]:
        print("{:2d}".format(d),end=" ")
        su+=abs(d)
    print()
print("\n\n")
print(su)
