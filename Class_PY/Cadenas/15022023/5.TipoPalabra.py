#5.Detetrminar que tipo de palabra es: aguda, grave, esdrujula sobre esdrujula.

a=str(input('Ingrese una palabra: '))

if a.endswith('án') or a.endswith('ón') or a.endswith('ún') or a.endswith('ás'):
    print('Es aguda')
else:
    print('xd')