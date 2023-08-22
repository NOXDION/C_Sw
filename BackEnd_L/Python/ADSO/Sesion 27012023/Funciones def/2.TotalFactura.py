'''Ejercicio 2
Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir 
la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.'''


def totalFactura(total, iva=21):
    """Función de aplica el IVA a una factura.
    Parametros
    amount: Es la cantidad sin IVA
    vat: Es el porcentaje de IVA
    Devuelve el total de la factura una vez aplicado el IVA. 
    """
    return total + total*iva/100

print(f'El total de la factura con iva de 10% es {totalFactura(1000,10)}')
print(f'El total de la factura con iva de 21% es {totalFactura(1000)}')
