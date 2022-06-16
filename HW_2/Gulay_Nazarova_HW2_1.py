#Task A :Kenar qiymetlerin cixarilmasi
def selection_(li): #sorting the list
    for i in range(len(li)-1):
        min_=i
        for j in  range(i+1,len(li)):
            if li[j]<li[min_]:
                min_=j
        if min_!=i:
            li[min_],li[i]=li[i],li[min_]
    return li


def my_func(li,n):
    li=selection_(li)
    if len(li)<2*n:
        return "You didn't enter enough values"
    return li[n:(len(li)-n)]



#liste ededlerin daxil edilmesi
A=[]
while True:
    a=input("Enter a value(blank to quit): ")
    if a!=" ":
        A+=[int(a)]
    if a==" ":
        break
B=A[:]

#n
while True:
    n=int(input("Enter the number of outliers to be removed:" ))
    if n>0:
        break
    
print("With the number of outliers to be removed:{}"\
      .format(my_func(A,n)))
print("The original data:{}".format(B))

