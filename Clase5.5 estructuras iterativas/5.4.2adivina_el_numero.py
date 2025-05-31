# Adivina el número.
# Genera un número aleatorio entre 1 y 100 y pide al usuario que lo adivine.
# El programa debe seguir pidiendo números hasta que acierte.
'''
clase:       5
Tema:        Estructuras iterativas
Ejercicio:   1
Descripción: 5.4.1. ¡Adivina el numero!

Autor:       Monica Alvarenga
Fecha:       2025-06-1
Estado:      [Terminado]
'''
import random

num = random.randrange(1,100)

for i in range(1,101):
    b=int(input("adivina el numero:"))
    if b>num:
        print("El numero secreto es menor")
    if b<num:
        print("El numero secreto es mayor")
    if b==num:
        print("LO ADIVINASTE!")
        break
    
