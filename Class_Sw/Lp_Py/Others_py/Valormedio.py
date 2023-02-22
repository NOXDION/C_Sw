n1= int(input('Numero 1: '))
n2= int(input('Numero 2: '))
n3= int(input('Numero 3: '))
menor= min(n1,n2,n3)
mayor= max(n1,n2,n3)
valor_medio= (n1+n2+n3)-menor-mayor
print('El valor medio es: ',valor_medio)
