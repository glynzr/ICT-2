#Task E
from random import uniform
def sum_(li):#instead of writing sum_(x_) and sum_(y_) we can write
    su=0    # sum_xy(x_,temp) and sum_xy(temp,y_) respectively
    for i in li: #temp=[1 for _ in range(n)]
        su+=i
    return su
    

def sum_xy(li_1,li_2):
    su=0
    for i in range(len(li_1)):
        su+=li_1[i]*li_2[i]
    return su

def sum_x(li):#instead of ths function we can use sum_xy(x_,x_) 
    su=0
    for i in li:
        su+=i**2
    return su


while True:
    n=int(input("Noqteleri sayi: "))
    if n>0:
        break

#x_=[round(uniform(0,5),2) for _ in range(n)]
#y_=[round(uniform(0,5),2) for _ in range(n)]
x_=[4.46,4.39,3.04]
y_=[2.24,0.23,1.47]

m=(sum_xy(x_,y_)-(sum_(x_)*sum_(y_))/n)/(sum_x(x_)-(sum_(x_)**2)/n)
b=sum_(y_)/n -(sum_(x_)/n)*m

print("f(x)={:.2f}*x+{:.2f}".format(m,b))

