#Exercise 24:Units of time
days,hours,minutes,seconds=map(int,input("Enter the duration in the sequence\
of days,hours,minutes,seconds:\n").split(":"))
print("{}:{:02d}:{:02d}:{:02d}".format(days,hours,minutes,seconds))
duration_in_seconds=seconds+minutes*60+hours*3600+days*24*3600
print("Duration in seconds={}".format(duration_in_seconds))
