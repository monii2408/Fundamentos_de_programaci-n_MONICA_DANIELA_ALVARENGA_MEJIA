'''
Clase:        Clase 10
Tema:         Matrices
Ejercicio:    10.3.1
Descripción:  Matriz simetrica

Autor:        Monica Daniela Alvarenga Mejia
Fecha:        2025-06-13
Estado:       [ Terminado ]
'''
matriz = int(input("ingrese el numero de columnas: "))
empty = []
for i in range(matriz):
    filas = list(map(int, input().split()))
    empty.append(filas)
    if len(filas)!=matriz:
        print("La matriz no es cuadrada")

# for m in range(len(empty)):
#     for n in range(len(empty[m])):
#         if empty[0][m]==empty[n][0]:
#             print(empty[0][m])
#         if empty[m][len(empty)+1]==empty[len(empty[m])+1][n]:
#             print(empty[m][0])
simetria=True
for m in range(matriz):
    for n in range(matriz):
        if empty[m][n]!=empty[n][m]:
            simetria = False

if simetria==True:
    print("La matriz es simetrica")
else:
    print("La matriz no es simetrica")
