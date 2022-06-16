#Task B Diaqonallarin muqayisesi
from random import randint
N=int(input("List olcusunu daxil edin: "))
A=[]
for i in range(N):
      A+=[[randint(1,10) for _ in range(N)]]
print("Random data")
for i in range(N):
    for b in A[i]:
          print("{:2d}".format(b),end="  ")
    print()





left_diaqonal=[]
right_diaqonal=[]

sum_left=0
sum_right=0


for i in range(N):
    left_diaqonal+=[A[i][i]]
    sum_left+=A[i][i]
print("Left diaqonal->{}->{}".format(left_diaqonal,sum_left))


for i in range(N):
    right_diaqonal+=[A[i][N-i-1]]
    sum_right+=A[i][N-1-i]
print("Right diaqonal->{}->{}".format(right_diaqonal,sum_right))



if sum_left>sum_right:
    print("Sum of right diaqonal is less than sum of right diaqonal")
elif sum_left<sum_right:
    print("Sum of left diaqonal is less than sum of right diaqonal")
else:
    print("Sum of right diaqonal is equal to  sum of left diaqonal")
