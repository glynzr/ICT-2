#9 Lab 8
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
B=[]
for x in range(n):
    RE=1
    for y in range(n):
        RE*=A[y][x]
    B+=[RE]
print(B)
        
