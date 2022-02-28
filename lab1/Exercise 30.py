
#Exercise 30:Units of pressure
pressure=float(input("Enter the pressure in kilopascals: "))
physical_atmospheres=round(pressure/101.32,2)
millimetres_of_mercury=round(pressure/0.133322,2)
pounds_per_square_inch=round(pressure/6.8948,2)
print("{}kPa={}atm".format(pressure,physical_atmospheres))
print("{}kPa={}mmHg".format(pressure,millimetres_of_mercury))
print("{}kPa={}psi".format(pressure,pounds_per_square_inch))
