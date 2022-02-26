#Exercise 39:Sound levels
noise=float(input("Enter a decibel level: "))
Jackhammer=130
Gas_lawnmower=106
Alarm_clock=70
Quiet_room=40
if noise>Jackhammer:
    print("It is loud noise")
elif noise==Jackhammer:
    print("This is  jacjhammer noise")
elif noise<Jackhammer and noise>Gas_lawnmower:
    print("This noise is between jackhammer's and gas lawnmower's noise")
elif noise==Gas_lawnmower:
    print("This is lawnmower noise")
elif Alarm_clock<noise<Gas_lawnmower:
    print("This noise is between alarm clock's and gas lawnmower's noise")
elif noise==Alarm_clock:
    print("This is alarm clock's noise")
elif Quiet_room<noise<Alarm_clock:
    print("This noise is between alarm clock's and quiet room's noise")
elif noise==Quiet_room:
    print("This is quiet room")
elif noise<Quiet_room:
    print("Too quiet place")
