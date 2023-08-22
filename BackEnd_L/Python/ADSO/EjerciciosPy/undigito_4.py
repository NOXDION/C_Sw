import random
vector=[int(random.random()*100) for i in range(10)]
digitos=[x if x<=9 else 0 for x in vector]
print(vector)
print(digitos)