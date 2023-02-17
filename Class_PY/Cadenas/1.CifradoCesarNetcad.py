'''-Solo acepta letras latinas (nota: los Romanos no usaban espacios en blanco ni dígitos).
-Todas las letras del mensaje están en mayúsculas (nota: los Romanos solo conocían 
las mayúsculas).'''

# Cifrado César.

text = input("Ingresa tu mensaje: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1 #Para decifrar el mensaje solo hay que cambiar el +1 por el -1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)
print(cipher)
