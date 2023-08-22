import random

lista=[]

for indice in range(30):
    lista.insert(indice,round(random.random(5,28)))
print(lista,"\nEl tamaño de la lista es: ", len(lista))

suma_mitad1=0
suma_mitad2=0

for indice in range(16):
    suma_mitad1+=lista[indice]
print('Promedio mitad 1: ',suma_mitad1/16)

for indice in range(15):
    suma_mitad2+=lista[indice]
print('Promedio mitad 2: ',suma_mitad2/10)

suma_tercio1=0
suma_tercio2=0
suma_tercio3=0

for indice in range(10):
    suma_tercio1+=lista[indice]
print('Promedio tercio 1: ',suma_tercio1/10)

for indice in range(11,21):
    suma_tercio2+=lista[indice]
print('Promedio tercio 2: ',suma_tercio2/10)

for indice in range(20,30):
    suma_tercio3+=lista[indice]
print('Promedio tercio 3: ',suma_tercio3/10)


