import random
cantidad=random.randint(1,5)
lista=[[int(random.randrange(100)) for i in range(cantidad) ] for i in range(random.randint(2,5))]
for i in lista:
    print(i)
    