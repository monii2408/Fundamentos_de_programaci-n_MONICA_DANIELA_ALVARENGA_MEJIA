#Eliminar duplicados

lista = list(map(int, input('ingrese los numeros a la lista:').split()))

sin_duplicados = []
for i in lista:
    if i not in sin_duplicados:
        sin_duplicados.append(i)
        print( i, end = " ")

