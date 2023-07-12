palabra = 'chupacabra'
print('Has entrado al juego')
while True:
    ingresar = input('Ingresa una palabra: ')
    if ingresar == palabra:
        break
    print('Sigues en el bucle')
print('¡Has ganado el juego!')

