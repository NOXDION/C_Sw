import random
vector=[int(random.random()*100) for i in range(10)]

pares=[x for x in vector if x%2==0]
impares=[x for x in vector if x%2!=0]
print(vector,"\n",pares,"\n",impares)

pares2=[x if x%2==0 else 0 for x in vector]
print(pares2)
