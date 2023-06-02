#Remplazar la ruleta del instructor

import random
estudiantes=['James','Joel','Luz','Sagrario','Dionigi']
ruleta=int(random.randint(0,4))
print(ruleta)
indice=estudiantes[ruleta]
print('El escogido es',indice)