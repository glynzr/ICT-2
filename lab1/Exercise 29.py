#Exercise 29:Celcius to Fahrenheit and Kelvin
celcius=float(input("Enter the temperature with celcius degree: "))
print(celcius)
kelvin=celcius+273
fahrenheit=(9*celcius)/5+32
print("{} celcius={} K".format(celcius,kelvin))
print("{} celcius={:.2f} F".format(celcius,fahrenheit))
