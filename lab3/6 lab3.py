#6 lab3
import random
even=[]
odd=[]
for x in random.sample(range(1,101),10):
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
print("Even: {}".format(even))
print("Odd: {}".format(odd))



