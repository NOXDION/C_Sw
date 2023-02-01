# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.
user_word = input("Ingrese algo: ")
user_word = user_word.upper()

for letter in user_word:
    # Completa el cuerpo del bucle for.
    if letter in 'AEIOU':
     continue
    print(letter)   
