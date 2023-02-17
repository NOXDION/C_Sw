#3.Cuantas veces se repite un caracter dado. 

cadena=str(input('Ingrese una cadena: '))

#def contarAbecedario2(cadena):
a=[]
b=[]
for character in cadena:
    if character not in a:
        a.append(character)
    elif character in a:
        b.append(character)
    #return len(cadena),len(a),len(b)

#print(contarAbecedario2(cadena))

print(a,b)