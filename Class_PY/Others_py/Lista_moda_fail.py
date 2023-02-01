import random

tam=random.randint(10,25)
list=[]

for indice in range(tam):
    list.insert(indice,round(random.random()*100))
print(list,"\nTamaño de la lista: ", len(list))

suma=0

for indice in range(len(list)):
    suma += list[indice]
print('La suma es: ',suma,'\nEl promedio es: ',suma//indice)

longi=(len(list))
cuenta=0 #contar las veces que se repite cada elemento
mayor=0

for i in range(longi):
    cuenta=0 #reinicia a cuenta antes de proceder a contar los siguientes elementos
    for j in range (longi):
        if list[i]==list[j]:
            cuenta += 1 #contar las ocurrencias del elemento
    if cuenta>mayor: #comparando en busca de la cuenta mayor
        mayor=cuenta #intercamnbio de variables
        moda=list[i]
print('La moda es: ',moda,'y se repite',mayor, 'veces.')
