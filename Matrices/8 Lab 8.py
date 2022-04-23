#8 Lab 8
from random import randint
while True:
    n=int(input("n= "))
    if n>0:
        break

A=[]
for i in range(n):
    A+=[[randint(-10,10) for _ in range(n)]]
    for a in A[i]:
        print("{:2d}".format(a),end=" ")
    print()
B=[]
for t in range(n):
    y=0
    for z in A[t]:
        y+=z
    B+=[y]
print(B)
