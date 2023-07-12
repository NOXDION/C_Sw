import random

tam=random.randint(10,25)
lista=[]

for indice in range(tam):
    lista.insert(indice,round(random.random()*100))
print(lista,"\nEl tamaño de la lista es: ", len(lista))

tam2=random.randint(10,25)
lista2=[]

for indice in range(tam2):
    lista2.append(round(random.random()*100))
print(lista2,"\nEl tamaño de la lista es: ", len(lista2))


lista3=[round(random.random()*100) for i in range (random.randint(10,25))]
print(lista3,"\nEl tamaño de la lista es: ", len(lista3))

lista4=[int(random.random()*100) for i in range (random.randint(10,25))]
print(lista4,"\nEl tamaño de la lista es: ", len(lista4))