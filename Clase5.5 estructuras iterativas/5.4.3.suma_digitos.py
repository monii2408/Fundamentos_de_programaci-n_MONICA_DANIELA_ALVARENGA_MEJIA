'''
clase:       5
Tema:        Estructuras iterativas
Ejercicio:   2
Descripción: 5.4.2. Sumador de valores posicionales

Autor:       Monica Alvarenga
Fecha:       2025-06-1
Estado:      [Terminado]
'''
numero = str(input("ingrese un numero: "))

while len(numero)>1:
    digits_sum = 0
    for digito in (numero):
        digits_sum=digits_sum+int(digito)
    print(f"{numero}= {digits_sum}")
    numero=str(digits_sum)
        
print("el resultado final es:", digits_sum)
