#slide 111 Task C
import random
li=[random.randint(1,5) for _ in range(7)]
print(li)
max_=li[0]
count=0
for i in range(len(li)):
    if max_<=li[i]:
        max_=li[i]
for x in range(len(li)):
    if li[x]==max_:
        count+=1
print("Maksimal qiymet:{}".format(max_))
print("Elementlerin sayi:{}".format(count))
