#slide 123 Task C
from random import randint
def IsFibo(N,x):
    li=[0,1]
    while True:
        li+=[li[-1]+li[-2]]
        if li[-1]>N:
            break
    if x in li:
        return True
    return False
N=int(input("N= "))
a=int(input("a= "))# indicates the number of random numbers in  a list
A=[randint(1,N) for _ in range(a)]
print(A)
B=[i for i in A if IsFibo(N,i)]
print(B)
