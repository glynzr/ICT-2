#Task A:Burcun teyin edilmesi
#1st method
print("Determine your Zodiac sign")
def Zodiac(m,n):
    m=m[0].upper()+m[1:].lower()
    a="Either a month or a day is invalid!"
    if m=="January" or m=="March" or m=="May" or m=="July" or m=="August" or m=="October" or m=="December"  or m=="February" or m=="April" or m=="June" or m=="September" or m=="November":
        if m=="December" and 22<=n<=31 or m=="January" and n<=19:
            b="Capricorn"
        elif m=="January" and 20<=n<=31 or m=="February" and n<=18:
            b="Aqurius"
        elif m=="February" and 19<=n<=29 or m=="March" and n<=20:
            b="Pisces"
        elif m=="March" and 21<=n<=31 or m=="April" and n<=19:
            b="Aries"
        elif m=="April" and 20<=n<=30 or m=="May" and n<=20:
            b="Taurus"
        elif m=="May" and 21<=n<=31 or m=="June" and n<=20:
            b="Gemini"
        elif m=="June" and 21<=n<=30 or m=="July" and n<=22:
            b="Cancer"
        elif m=="July" and 23<=n<=31 or m=="August" and n<=22:
            b="Leo"
        elif m=="August" and 23<=n<=31 or m=="September" and n<=22:
            b="Virgo"
        elif m=="September" and 23<=n<=30 or m=="October" and n<=22:
            b="Libra"
        elif m=="October" and 23<=n<=31 or m=="November" and n<=21:
            b="Scorpio"
        elif m=="November" and 22<=n<=30 or m=="December" and n<=21:
            b="Sagittarius"
        else:
            return a
        c="Your Zodiac sign is "+b
        return c
    else:
        return a
m=input("Enter month[ex.March]: ")
n=int(input("Enter the day[ex.12]: "))
print(Zodiac(m,n))


#2nd method
"""
print("Determine your Zodiac sign")
m=input("Enter month[ex.March]: ")
n=int(input("Enter the day[ex.12]: "))

m=m[0].upper()+m[1:].lower()
a="Either a month or a day is invalid!"
if m=="January" or m=="March" or m=="May" or m=="July" or m=="August" or m=="October" or m=="December"  or m=="February" or m=="April" or m=="June" or m=="September" or m=="November":
    flag=True
    if m=="December" and 22<=n<=31 or m=="January" and n<=19:
        b="Capricorn"
    elif m=="January" and 20<=n<=31 or m=="February" and n<=18:
        b="Aqurius"
    elif m=="February" and 19<=n<=29 or m=="March" and n<=20:
        b="Pisces"
    elif m=="March" and 21<=n<=31 or m=="April" and n<=19:
        b="Aries"
    elif m=="April" and 20<=n<=30 or m=="May" and n<=20:
        b="Taurus"
    elif m=="May" and 21<=n<=31 or m=="June" and n<=20:
        b="Gemini"
    elif m=="June" and 21<=n<=30 or m=="July" and n<=22:
        b="Cancer"
    elif m=="July" and 23<=n<=31 or m=="August" and n<=22:
        b="Leo"
    elif m=="August" and 23<=n<=31 or m=="September" and n<=22:
        b="Virgo"
    elif m=="September" and 23<=n<=30 or m=="October" and n<=22:
        b="Libra"
    elif m=="October" and 23<=n<=31 or m=="November" and n<=21:
        b="Scorpio"
    elif m=="November" and 22<=n<=30 or m=="December" and n<=21:
        b="Sagittarius"
    else:
        flag=False
else:
    flag=False
print("Your zodiac sign is "+b if flag==True else  a)"""
