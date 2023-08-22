import random

def llenarLista(list):
    tam=round(random.randint(5,20))
    for i in range(tam):
        list.append(round(random.randrange(5,20)))
    return list

def sumarLista(list):
    suma=0
    for i in list:
        suma+=i
    return suma

lista=[]
lista=llenarLista(lista)
print(lista)
print('La suma es=',sumarLista(lista))