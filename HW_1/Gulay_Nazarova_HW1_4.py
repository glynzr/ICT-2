#Task D:Bax ve nomreleri soyle
print("Look and Say Numbers")
while True:
    N=int(input("Enter a number(N>0): "))
    if N>0:
        break


b=N
count_digit=0 #ededin reqemlerinin sayi
Result=""
#reqemlerin sayinin tapilmasi
while N>0:
    count_digit+=1
    N//=10

#reqem sayinin tek ve ya cut olmasi
if count_digit%2!=0:
    print("Invalid")
else:
    while b>0:
        x=b%100 #reqemleri sondan baslayaraq 2-2 secirik
        Result+=str(x%10)*(x//10)
        b//=100
    print(int(Result[::-1]))
    
    

