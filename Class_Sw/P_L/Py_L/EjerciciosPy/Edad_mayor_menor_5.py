import random

tam=random.randint(10,25)
vector=[int(random.random()*100) for i in range(tam)]
edad=['Mayor de edad' if x>=18 else 'menor de edad' for x in vector]


print(vector)
print(edad)
