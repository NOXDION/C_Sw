#A continuación presentamos el juego con el fin de analizar qué tan animal eres

ingresar=int(input('Presiona 1 para ingresar 0 para salir: '))
correctas=0
incorrectas=0

while ingresar==1:
    print('Responde todas las preguntas en minuscula')
    primera=input('1.¿Cuál es la etnia indígena más numerosa de Colombia? R/')
    if primera=='wayuu':
        print('Respondiste correctamente')
        correctas+=1
    else:
        print("Esta incorrecto maldito animal, es wayuu.")
        incorrectas+=1
    segunda=input('2.¿Hasta que año Panamá formó parte de Colombia? R/')
    if segunda=='1903':
        print('Respondiste correctamente')
        correctas+=1
    else:
        print("Esta incorrecto maldito animal, Panamá decretó su independencia y se separó de Colombia el 3 de noviembre de 1903.")
        incorrectas+=1
    tercera=input('3.¿Con cuántos países comparte Colombia fronteras terrestres? R/')
    if tercera=='5':
        print('Respondiste correctamente')
        correctas+=1
    else:
        print("Esta incorrecto maldito animal, son 5 ya que comparte fronteras y límites terrestres con Brasil, Perú, Ecuador, Panamá y Venezuela.")
        incorrectas+=1
    cuarta=input('4.¿Cuál es la capital del Departamento de Amazonas? R/')
    if cuarta=='leticia':
        print('Respondiste correctamente')
        correctas+=1
    else:
        print("Esta incorrecto maldito animal, la ciudad de Leticia es la capital del Departamento de Amazonas.")
        incorrectas+=1
    break
print(f'Respondiste {correctas} preguntas correctamente y {incorrectas} preguntas incorrectamente.')

while ingresar==0:
    print('Como te atreves a irte sin responder maldito animal.')
    break
