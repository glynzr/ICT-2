#Task C: Ededin reqemleri cemi ve hasili
import random
eded=random.randint(1000,9999)
d1=eded//1000
d2=(eded//100)%10
d3=(eded//10)%10
d4=eded%10
cem=d1+d2+d3+d4
hasil=d1*d2*d3*d4
print(eded)
print(d1, d2, d3, d4)
print("Cem:{} ".format(cem))
print("Hasil:{} ".format(hasil))
