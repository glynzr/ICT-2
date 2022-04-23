#3 Lab 8
from random import randint
while True:
    n=int(input("n= "))
    if n>0:
        break
A=[]
B=[]
for i in range(n):
    A+=[[randint(-10,10) for _ in range(n)]]
    B+=[[randint(-10,10) for _ in range(n)]]


C=[]
D=[]
for a in range(n):
    C+=[[0]*n]
    D+=[[0]*n]

for t in range(n):
    for z in range(n):
        C[t][z]=A[t][z]**2+B[t][z]**2
        D[t][z]=A[t][z]**2-B[t][z]**2
print(A)
print(B)
print(C)
print(D)
print("\n")

for b in range(n):
    for b_ in C[b]:
        print("{:2d}".format(b_),end=" ")
    print()
print("\n")
for c in range(n):
    for c_ in D[c]:
        print("{:2d}".format(c_),end=" ")
    print()
 
