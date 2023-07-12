import random

tam = int(input("Ingrese la cantidad: "))

vec = []

for i in range (tam):
    vec.insert(i,round(random.random()*100))
    
print(vec)

contpar = 0
continpar = 0
sumapar = 0
sumaimpar = 0

for i in range(len(vec)):
    if vec[i] % 2 == 0:
        contpar += 1
        sumapar += vec[i]
        print("índice:",i,"valor:",vec[i],"es par")
    else:
        continpar += 1
        sumaimpar += vec[i]
        print("índice",i,"valor:",vec[i],"es impar")
        
print("\npares:", contpar, "\nimpares:",continpar)
print('\nsuma de los pares:',sumapar, '\nsuma de los impares:',sumaimpar)
print("\nPromedio de los pares es: ",sumapar // contpar,'\nPromedio de los impares es: ',sumaimpar // continpar)