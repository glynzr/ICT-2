#Task E:Onluq ve ikilik palindrom
print("Decimal and Binary Polindroms")
def Convert_to_Binary(N):
    bi=""
    while N>0:
        bi+=str(N%2)
        N//=2
    bi=bi[::-1]
    return bi

while True:
    N=int(input("Enter a number (N>0): "))
    if N>0:
        break
    
print("Decimal->{}".format(N))
print("Binary->{}".format(Convert_to_Binary(N)))

a=Convert_to_Binary(N)



def Polindrom(N,a):
    N=str(N)
    
    if N==N[::-1] and a==a[::-1]:
        print("Polindron type is Decimal and Binary")
    elif N==N[::-1]:
        print("Polidron type is only Decimal")
    elif a==a[::-1]:
        print("Polidron type is only Binary")
    else:
        print("Polindron type is neither Decimal nor Binary")
Polindrom(N,a)

