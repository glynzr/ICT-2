#4 Lab 8
from random import randint
while True:
    n,m,k=map(int,input("n,m,k= ").split(","))
    if n>0 and m>0 and n>k>0:
        break
A=[]
for i in range(n):
    A+=[[randint(-10,10) for _ in range(m)]]
print(A)

for b in range(n):
    for d in A[b]:
        print("{:2d}".format(d),end=" ")
    print()

RE=1
for a in A[k-1]:
    RE*=a
print(RE)
    
