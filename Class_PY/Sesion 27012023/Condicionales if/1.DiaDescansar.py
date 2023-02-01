'''Ejercicio 1
Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si 
es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir 
otro mensaje.'''

dia=input('Dia de la semana: ')
if (dia=='lunes'or dia=='martes'or dia=='miercoles' or dia=='jueves'):
    print('Oh, no!')
elif (dia=='viernes'):
    print('¡Ya casi!')
elif (dia=='sábado' or 'domingo'):
    print('Ahora sí se puede descansar')
