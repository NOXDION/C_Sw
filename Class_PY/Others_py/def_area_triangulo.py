def a_triangulo(base,altura):
    area = float(base*altura/2)
    return area

base=float(input('Ingrese base: '))
altura=float(input('Ingrese altura: '))

print(a_triangulo(base,altura))