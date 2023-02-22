'''Ejercicio 2
Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, 
que sean bisiestos y múltiplos de 10. Nota: para que un año sea bisiesto debe ser divisible por 4 y 
no debe ser divisible por 100, excepto que también sea divisible por 400.'''

añoInicio=int(input("Año inicial:"))
añoFin=int(input("Año final:"))
for año in range(añoInicio, añoFin+1):
   if año%10!=0:
       continue
   if año%4!=0:
       continue
   if año%100!=0 or año%400==0:
       print(año)