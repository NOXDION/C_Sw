year = int(input("Introduce un año: "))
if year < 1582:
    print('No dentro del período del calendario Gregoriano')
elif year % 4:
    print('Año comun')
elif year % 100:
    print('Año bisisesto')
elif year % 400:
    print('Año comun')
else:
    print('Año bisiesto')