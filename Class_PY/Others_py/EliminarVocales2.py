﻿word_without_vowels = ""

# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.

user_word = input("Ingrese algo: ")
user_word = user_word.upper()

for letter in user_word:
   # Completa el cuerpo del bucle.
    if letter in 'AEIOU':
     continue
    word_without_vowels+=letter
print(word_without_vowels)

# Imprimir la palabra asignada a word_without_vowels.
