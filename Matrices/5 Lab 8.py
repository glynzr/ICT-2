#5 Lab 8
from random import randint
while True:
    n,k,m=map(int,input("n,k,m= ").split(","))
    if n>k>0 and n>m>0:
        break

A=[]
for i in range(n):
    A+=[[randint(1,15) for _ in range(n)]]
    for a in A[i]:
        print("{:2d}".format(a),end=" ")
    print()
        
B=[]

for x in range(n):
    B+=[A[k-1][x]*A[x][m-1]]
print(B)
