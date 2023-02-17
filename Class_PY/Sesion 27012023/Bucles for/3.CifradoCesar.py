'''Ejercicio 3
Crear un programa para que el usuario pueda ingresar una palabra y encriptarla en el 
cifrado cesar con un dezplazamiento de 3 letras'''


'''alf=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
palabra=input('=')
for palabra in range(4):
    print(palabra)'''


alf=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
palabra =input('Ingrese una palabra en minuscula para cifrar: ')
cifrado = ""

for letra in palabra:
    indice = alf.index(letra)
    nuevo_indice = (indice + 3)%27
    nueva_letra = alf[nuevo_indice]
    cifrado += nueva_letra

print(f'El cifrado de {palabra} es {cifrado}')

