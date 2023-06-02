import random

t_primos=tuple(int(random.random()*100) for i in range (random.randint(10,25)))
print(t_primos,"\nEl tamaño de la lista es: ", len(t_primos))

primos = []

for i in range(len(t_primos)):
    divisores = 0
    for j in range(1,101):
        if t_primos[i] % j == 0:
            divisores += 1
    if divisores == 2:
        primos.append(t_primos[i])
print("Hay",len(primos),"números primos","\nSon los siguientes: ",tuple(primos))