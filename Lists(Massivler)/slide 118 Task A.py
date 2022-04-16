#slide 118 Task A
li=[1,2,3,4,5,6]
c=li[-1]
for x in range(len(li)-2,-1,-1):
    li[x+1]=li[x]
li[0]=c
print(li)
