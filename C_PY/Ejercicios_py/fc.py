def formulaCuadratica():
    import math
    try:
        a=float(input('Ingrese un numero: '))
        b=float(input('Ingrese un numero: '))
        c=float(input('Ingrese un numero: '))
        x_positiva= -b+math.sqrt(b**2-4*a*c)/(2*a)
        x_negativa= -b-math.sqrt(b**2-4*a*c)/(2*a)
        print(x_positiva)
        print(x_negativa)
    except ZeroDivisionError:
        print('No divida en 0')
    except ValueError:
        print('Numero imaginario')

formulaCuadratica()

def semana():
    try:
        dia=float(input('Ingrese el numero de dia: '))
        sem=['lunes','marte','miercoels','jueves','viernes']
        print(sem[dia])
    except IndexError:
        print('No existe ese dia de la semana')
    except TypeError:
        print('Que es esto?')

semana()

try:
    blog_posts = [{'Photos': 3, 'Megusta': 21, 'comentarios': 2}, 
    {'Megusta': 13, 'comentarios': 2, 'compartido': 1}, 
    {'Photos': 5, 'Megusta': 33, 'comentarios': 8, 'compartido': 3}, 
    {'comentarios': 4, 'compartido': 2}, 
    {'Photos': 8, 'comentarios': 1, 'compartido': 1}, 
    {'Photos': 3, 'Megusta': 19, 'comentarios': 3}]

    total_Megusta = 0

    for post in blog_posts:
        total_Megusta = total_Megusta + post['Megusta']
except KeyError:
    print('Error de llaves')

