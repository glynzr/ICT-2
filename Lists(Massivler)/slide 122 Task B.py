#slide 122 Task B
from random import randint
def isPrime(N):
    if N==1:
        return False
    for x in range(2,N):
        if N%x==0:
            return False
    if N==2:
        return True
    return True
            
while True:
    N=int(input("N= "))
    if N>0:
        break

A=[randint(0,100) for _ in range(N)]
print(A)
B=[x for x in A if isPrime(x)==True]
print(B)
