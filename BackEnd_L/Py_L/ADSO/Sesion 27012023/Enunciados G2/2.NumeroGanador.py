#Adivina el numero ganador

import random
NumeroAdivinar=random.randint(1,20)
print(NumeroAdivinar)
ingreso=int(input('Ingresa un numero del 1 al 20: '))
while ingreso != NumeroAdivinar:
    print('Sigues sin adivinar el numero')
    ingreso=int(input('Ingresa un numero del 1 al 20: '))
    if ingreso==NumeroAdivinar:
        break
print('Adivinaste el numero, has sido el ganador.')