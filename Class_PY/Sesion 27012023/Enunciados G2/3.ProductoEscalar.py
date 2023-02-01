#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos tuplas 
# y muestre por pantalla su producto escalar.

vector1=(1,2,3)
vector2=(-1,0,2)
ProductoEscalar=(vector1[0]*vector2[0])+(vector1[1]*vector2[1])+(vector1[2]*vector2[2])
print(f"El producto escalar entre el vector 1 {vector1} y el vector 2 {vector2} es: {ProductoEscalar}")

'''a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
for i in range(len(a)):
    product += a[i]*b[i]
print("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str(product))'''