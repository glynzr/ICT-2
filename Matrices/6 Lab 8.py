#6 Lab 8
from random import randint
while True:
    n,k=map(int,input("n,k= ").split(","))
    if n>k>0:
        break
A=[]
for i in range(n):
    A+=[[randint(-10,10) for _ in range(n)]]
    for a in A[i]:
        print("{:2d}".format(a),end=" ")
    print()
B=[]
for a in range(n):
    B+=[A[a][a]*A[k-1][a]]
print(B)
