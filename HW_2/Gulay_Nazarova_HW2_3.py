#Task C Orta qiymetden yuxari ve asagi olan ededler
A=[]
while True:
    a=input("Enter a number-[blank to quit]->")
    if a!=" ":
        A+=[int(a)]
    if a==" ":
        break


print("A list of numbers:")
print(A)

su=0
for i in A:
    su+=i
    
average=su/len(A)
print("Average value:{:.3f}".format(average))

A_high=""
A_average=""
A_less=""

for i in A:
    if i>average:
        A_high+=str(i)+" "
    elif i==average:
        A_average+=str(i)+" "
    else:
        A_less+=str(i)+" "
        
print("Less than Average:"+A_less)
print("Average: " if len(A_average)==0 else "Average:"+A_average )
print("Higher than Average:"+A_high)

