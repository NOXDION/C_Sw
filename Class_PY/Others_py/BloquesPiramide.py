blocks = int(input("Ingresa el número de bloques: "))

# Escribe tu código aquí.
height=0
while blocks>height:
    height += 1
    blocks -= height

print("La altura de la pirámide:", height)
