arroba = '@'
cantidad = 0
email = str(input('Ingrese su email: '))

for x in email:
    if x == '@':
        cantidad += 1

if cantidad ==1:
    print('Email correcto')
else:
    print('Email incorrecto')