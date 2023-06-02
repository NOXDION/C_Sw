def divisores(num):
    suma=0
    for i in range(1,num):
        if num%i==0:
            suma+=i
    return suma

def pefectos(num):
    sum=divisores(num)
    if sum==num:
        return 'Es perfecto'
    else:
        return 'No es perefecto'

def amigos(a,b):
    suma_a=divisores(a)
    suma_b=divisores(b)
    print(suma_a,suma_b)
    if suma_b == a:
        return 'Son amigos'
    elif suma_a == b:
        return 'Son amigos'
    else:
        return 'No son amigos'

#print(amigos(220,284))

'''def primos(num):
    for i in range(1,num+1):
        divisores=0
        for j in range(1,num+1):
            if i% j == 0:
                divisores += 1

    if divisores==2:
        return 'El numero es primo.'
    else:
        return 'El numero no es primo.' '''

def primos(num):
    suma_p=divisores(num)
    if suma_p==1:
        return 'Es primo'
    else:
        return 'No es primo'

print(primos(53))