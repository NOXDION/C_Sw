def convertidor(c):
    f = 9/5 * c + 32
    k = c + 273.15
    r = c*9/5 + 491.67
    print(c,' grados celsius equivale a ',f,' grados fahrenheit.')
    print(c,' grados celsius equivale a ',k,' grados kelvin.')
    print(c,' grados celsius equivale a ',r,' grados rankine.')

c=float(input('Ingrese un numero: '))
convertidor(c)
