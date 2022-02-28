#Exercise 25:Units of time(again):
total_seconds=int(input("Enter the total duration in seconds: "))
days=total_seconds//(24*3600)
hours=(total_seconds%(24*3600))//3600
minutes=((total_seconds%(24*3600))%3600)//60
seconds=((total_seconds%(24*3600))%3600)%60
print("{} seconds={}:{:02d}:{:02d}:{:02d}".format(total_seconds\
        ,days,hours,minutes,seconds))

