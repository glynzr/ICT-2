#slide 110 Task A
import random
li=[random.randint(1,5) for _ in range(5)]
print(li)
max_=li[0]
min_=li[0]
a=""
b=""
for i in range(len(li)):
    if max_<li[i]:
        max_=li[i]
    if min_>li[i]:
        min_=li[i]
    
for x in range(len(li)):
    if li[x]==max_:
         a+="A["+str(x)+"]="+str(max_)+" "
    if li[x]==min_:
        b+="A["+str(x)+"]="+str(min_)+" "
print("Max:",a)
print("Min:",b)

