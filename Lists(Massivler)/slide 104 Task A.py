#slide 104 Task A
import random
A=[random.randint(0,5) for i in range(10)]
print(A)
a=int(input("Ne axtaririq? "))
if a in A:
    for x in range(len(A)):
        if A[x]==a:
            print("A[{}]={}".format(x,a),end=" ")
else:
    print("Tapilmadi")
    





